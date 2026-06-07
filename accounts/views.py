from django.shortcuts import render, redirect, get_object_or_404
from django.utils import timezone
from django.contrib import messages

from .models import User

def login_view(request):
    if request.method == "POST":
        u = User.objects.filter(login_id=request.POST.get("login_id"),
                                password=request.POST.get("password")).first()
        if u:
            request.session['user_id'] = u.id
            request.session['role'] = u.role.role_name
            request.session['employee_no'] = u.employee_no
            request.session['romobile_nole'] = u.mobile_no
            request.session['officer_name'] = u.officer_name
            request.session['circle'] = u.circle
            request.session['division'] = u.division
            request.session['role_id'] = u.role.id
            if u.role.id == 1:
                return redirect('dashboard')
            else:
                return redirect('dashboard_officer')
    return render(request, "login.html")

def dashboard(request):
    if not request.session.get('user_id'):
        return redirect('login')
    return render(request, "dashboard.html")



def logout_view(request):
    request.session.flush()
    return redirect('login')

def dashboard_officer(request):
    if not request.session.get('user_id'):
        return redirect('login')
    return render(request, "dashboard_officer.html")