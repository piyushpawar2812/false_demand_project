
import requests
from django.shortcuts import render, redirect, get_object_or_404
from django.utils import timezone
from django.contrib import messages
from django.http import JsonResponse
from .models import FalseDemandRequest,LocationDetails
from accounts.models import User
from datetime import datetime


def false_demand_form(request):
    if not request.session.get('user_id'):
        return redirect('login')

    data = None
    error = None
    success = None

    def fetch_consumer_data(consumer_no):
        url = f"http://ngbmisapp2.mpcz.in:8090/Mri-Ngb/api/ngb/getConsumerData?consumerNo={consumer_no}"
        res = requests.get(url)
        return res.json()

    if request.method == "POST":

        # 🔍 SEARCH
        if "fetch" in request.POST:
            consumer_no = request.POST.get("consumer_no")

            if not consumer_no:
                error = "Consumer Number is required!"
            else:
                try:
                    response = fetch_consumer_data(consumer_no)

                    if response.get("code") == "200" and response.get("list"):
                        data = response["list"][0]
                    else:
                        error = "No data found"

                except Exception as e:
                    error = str(e)

        # ✅ SUBMIT (SAVE TO DB)
        elif "submit" in request.POST:

            try:
                location_code = request.POST.get('location_code')
                print("location_code---------",location_code)

                # 🔍 LocationDetails se match karo
                location = LocationDetails.objects.filter(code=location_code).first()
                print("location---------",location)
                # Default values
                circle_id = ''
                division_id = ''

                if location:
                    circle_id = location.circle_id
                    division_id = location.division_id

                request_id = int(datetime.now().strftime("%Y%m%d%H%M%S"))
                FalseDemandRequest.objects.create(
                    name=request.POST.get("name"),
                    mobile=request.POST.get("mobile"),
                    address=request.POST.get("address"),
                    city=request.POST.get("city"),
                    state=request.POST.get("state"),
                    terrif_code=request.POST.get("terrif_code"),
                    location_code=request.POST.get("location_code"),
                    requested_amount=request.POST.get("amount"),
                    document=request.FILES.get("document"),
                    
                    # 👇 ye tumhe set karna padega (example)
                    circle_id=circle_id,
                    division_id=division_id,
                    request_id=request_id,
                    consumer_no = request.POST.get("consumer_no")
                )

                success = "Request submitted successfully!"
                data = None  # form reset

            except Exception as e:
                error = "Save Error: " + str(e)

    return render(request, "false_demand_form.html", {
        "data": data,
        "error": error,
        "success": success
    })

def save_false_demand(request):
    if request.method == "POST":

        user = User.objects.first()  # ya logged-in user use karo

        location_code = request.POST.get('location_code')

        # 🔍 LocationDetails se match karo
        location = LocationDetails.objects.filter(code=location_code).first()

        # Default values
        circle_id = ''
        division_id = ''
        region_id = ''

        if location:
            circle_id = location.circle_id
            division_id = location.division_id

        print("---------",circle_id)
        print("---------",circle_id)
        FalseDemandRequest.objects.create(
            name=request.POST.get('name'),
            mobile=request.POST.get('mobile'),
            address=request.POST.get('address'),
            city=request.POST.get('city'),
            state=request.POST.get('state'),
            terrif_code=request.POST.get('terrif_code'),
            location_code=location_code,

            requested_amount=request.POST.get('amount'),
            document=request.FILES.get('document'),

            # 🔥 DB se liya hua data
            circle_id=circle_id,
            division_id=division_id
            # agar model me region_id add karna ho to yaha bhi add karo
        )

    return redirect('request_list')


def request_list(request):
    if not request.session.get('user_id'):
        return redirect('login')
    data = FalseDemandRequest.objects.all().order_by('-id')
    return render(request, "request_list.html", {"data": data})


# def user_request_details(request):
#     if not request.session.get('user_id'):
#         return redirect('login')
#     officer_data = User.objects.filter(id=request.session.get('user_id'))

#     data = FalseDemandRequest.objects.filter(circle_id=request.session.get('circle'),division_id=request.session.get('division'))
#     return render(request, "user_request_details.html", {"data": data})

def user_request_details(request):
    if not request.session.get('user_id'):
        return redirect('login')

    # ✅ Session values (safe casting)
    try:
        circle_id = int(request.session.get('circle'))
        division_id = int(request.session.get('division'))
        role_id = int(request.session.get('role_id'))
    except (TypeError, ValueError):
        return redirect('login')

    # ✅ Base Query
    base_qs = FalseDemandRequest.objects.filter(
        circle_id=circle_id,
        division_id=division_id
    )

    # ✅ Role-based filtering (clean & non-overlapping)
    if role_id in [3,8]: # 3 AO1--- 8 CGM1                           # 1----oag1(Creator)
        # Only high amount
        data = base_qs.filter(requested_amount__gte=500000)

    elif role_id in [4, 5]: # 4	DGMONM1 --- 5 DGMVIG1
        # See all (both high & low)
        data = base_qs

    elif role_id in [7, 11]:# 11	GM1 --7	ZONAL1

        # Low 500000
        data = base_qs.filter(requested_amount__lt=500000)

    else:
        # No access
        data = base_qs.none()

    return render(request, "user_request_details.html", {"data": data})


def form_view(request, pk):
    if not request.session.get('user_id'):
        return redirect('login')
    data = get_object_or_404(FalseDemandRequest, id=pk)
    return render(request, "form_view.html", {"data": data})

from django.shortcuts import render, redirect, get_object_or_404
from django.utils import timezone
from django.contrib import messages

def user_form_view(request, pk):
    if not request.session.get('user_id'):
        return redirect('login')

    data = get_object_or_404(FalseDemandRequest, id=pk)

    role_id = request.session.get("role_id")

    # 🔑 Map role to fields (clean approach)
    role_map = {
        8: ("cgm_status", "cgm_remark", "cgm_doc", "cgm_date_time", "cgm_name_mobile"),
        3: ("ao_status", "ao_remark", "ao_doc", "ao_date_time", "ao_name_mobile"),
        4: ("dgm_onm_status", "dgm_onm_remark", "dgm_onm_doc", "dgm_onm_date_time", "dgm_onm_name_mobile"),
        5: ("dgm_vig_status", "dgm_vig_remark", "dgm_vig_doc", "dgm_vig_date_time", "dgm_vig_name_mobile"),
        11: ("gm_status", "gm_remark", "gm_doc", "gm_date_time", "gm_name_mobile"),
        7: ("zonal_officer_status", "zonal_officer_remark", "zonal_officer_doc", "zonal_officer_date_time", "zonal_officer_name_mobile"),
    }

    # ❌ Invalid role safety
    if role_id not in role_map:
        messages.error(request, "Unauthorized access")
        return redirect('dashboard')

    status_field, remark_field, doc_field, dt_field, name_field = role_map[role_id]

    # 🔒 BLOCK: already submitted by THIS ROLE
    if getattr(data, status_field) in [1, 2, 3]:
        messages.warning(request, "You have already submitted your action.")
        return render(request, "user_form_view.html", {
            "data": data,
            "already_submitted": True
        })

    if request.method == "POST":
        status = int(request.POST.get("status"))
        remark = request.POST.get("remark")
        document = request.FILES.get("upload_doc")

        officer_name = request.session.get("officer_name")
        mobile = request.session.get("romobile_nole")
        name_mobile = f"{officer_name} ({mobile})"

        # ✅ Save dynamically
        setattr(data, status_field, status)
        setattr(data, remark_field, remark)
        setattr(data, doc_field, document)
        setattr(data, dt_field, timezone.now())
        setattr(data, name_field, name_mobile)
        status_values = [
            data.cgm_status,
            data.ao_status,
            data.dgm_onm_status,
            data.dgm_vig_status,
            data.gm_status,
            data.zonal_officer_status,
        ]

        # ❌ Priority 1: Reject
        if 2 in status_values:
            data.final_puss_status = 2

        # ❌ Priority 2: Revert
        elif 3 in status_values:
            data.final_puss_status = 3

        # ✅ Priority 3: 4 approvals
        elif status_values.count(1) >= 4:
            data.final_puss_status = 1

        # ⏳ Pending
        else:
            data.final_puss_status = 0


        data.save()

        messages.success(request, "Form submitted successfully ✅")
        return redirect('user_request_details')
    status_list = [
    ("AO", data.ao_status),
    ("DGM ONM", data.dgm_onm_status),
    ("DGM VIG", data.dgm_vig_status),
    ("Zonal Officer", data.zonal_officer_status),
    ("GM", data.gm_status),
    ("CGM", data.cgm_status),
]


    return render(request, "user_form_view.html", {
        "data": data,
        "already_submitted": False,
        "status_list": status_list
    })







def mis_report(request):

    data = FalseDemandRequest.objects.all().order_by('-id')

    # Create lookup dictionaries

    circle_map = {}
    division_map = {}

    locations = LocationDetails.objects.all()

    for loc in locations:

        circle_map[str(loc.circle_id)] = loc.circle_name

        division_map[str(loc.division_id)] = loc.division_name


    # Attach readable names

    for i in data:

        i.circle_name = circle_map.get(str(i.circle_id), '-')

        i.division_name = division_map.get(str(i.division_id), '-')


    context = {
        'data': data
    }

    return render(request, 'mis_report.html', context)


