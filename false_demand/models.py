from django.db import models

class FalseDemandRequest(models.Model):
    name = models.CharField(max_length=200)
    mobile = models.CharField(max_length=15)
    address = models.TextField()
    city = models.CharField(max_length=100)
    state = models.CharField(max_length=100)
    location_code = models.CharField(max_length=100)
    requested_amount = models.BigIntegerField()
    document = models.FileField(upload_to='docs/')
    circle_id = models.CharField(max_length=100)
    division_id = models.CharField(max_length=100)
    request_id = models.BigIntegerField(null=True, blank=True)
    consumer_no = models.BigIntegerField(null=True, blank=True)  
    terrif_code= models.CharField(max_length=100,blank=True)

# CGM

    cgm_status = models.IntegerField(default=0)  # default 0 ya 9 tum set kar sakte ho
    cgm_remark = models.CharField(max_length=255, null=True, blank=True)
    cgm_date_time = models.DateTimeField(null=True, blank=True)
    cgm_doc = models.FileField(upload_to='cgm_docs/', null=True, blank=True)
    cgm_name_mobile = models.CharField(max_length=255, null=True, blank=True)

    # AO
    ao_status = models.IntegerField(default=0)
    ao_remark = models.CharField(max_length=255, null=True, blank=True)
    ao_date_time = models.DateTimeField(null=True, blank=True)
    ao_doc = models.FileField(upload_to='ao_docs/', null=True, blank=True)
    ao_name_mobile = models.CharField(max_length=255, null=True, blank=True)

    # DGM_ONM
    dgm_onm_status = models.IntegerField(default=0)
    dgm_onm_remark = models.CharField(max_length=255, null=True, blank=True)
    dgm_onm_date_time = models.DateTimeField(null=True, blank=True)
    dgm_onm_doc = models.FileField(upload_to='dgm_onm_docs/', null=True, blank=True)
    dgm_onm_name_mobile = models.CharField(max_length=255, null=True, blank=True)


    # DGM_VIG
    dgm_vig_status = models.IntegerField(default=0)
    dgm_vig_remark = models.CharField(max_length=255, null=True, blank=True)
    dgm_vig_date_time = models.DateTimeField(null=True, blank=True)
    dgm_vig_doc = models.FileField(upload_to='dgm_vig_docs/', null=True, blank=True)
    dgm_vig_name_mobile = models.CharField(max_length=255, null=True, blank=True)


    # GM
    gm_status = models.IntegerField(default=0)
    gm_remark = models.CharField(max_length=255, null=True, blank=True)
    gm_date_time = models.DateTimeField(null=True, blank=True)
    gm_doc = models.FileField(upload_to='gm_docs/', null=True, blank=True)
    gm_name_mobile = models.CharField(max_length=255, null=True, blank=True)


    # ZONAL OFFICER
    zonal_officer_status = models.IntegerField(default=0)
    zonal_officer_remark = models.CharField(max_length=255, null=True, blank=True)
    zonal_officer_date_time = models.DateTimeField(null=True, blank=True)
    zonal_officer_doc = models.FileField(upload_to='zo_docs/', null=True, blank=True)
    zonal_officer_name_mobile = models.CharField(max_length=255, null=True, blank=True)
    final_puss_status = models.IntegerField(default=0)


class LocationDetails(models.Model):
    circle_name = models.CharField(max_length=255)
    division_name = models.CharField(max_length=255)
    zone_name = models.CharField(max_length=255)

    code = models.IntegerField(null=True, blank=True)  
    name = models.CharField(max_length=255, null=True, blank=True)
    division_id = models.IntegerField(null=True, blank=True)  

    short_code = models.CharField(max_length=50, null=True, blank=True)
    address = models.TextField(null=True, blank=True)
    phone_no = models.CharField(max_length=20, null=True, blank=True)

    circle_id = models.IntegerField(null=True, blank=True)  
    region_id = models.CharField(max_length=50, null=True, blank=True)

    def __str__(self):
        return f"{self.circle_name} - {self.division_name}"