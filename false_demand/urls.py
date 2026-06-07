
from django.urls import path
from . import views

urlpatterns = [
    path('false-demand/', views.false_demand_form, name='false_demand_form'),
    # path('get-consumer-data/', views.get_consumer_data),
    path('save/', views.save_false_demand, name='save_false_demand'),
    path('request-list/', views.request_list, name='request_list'),
    

    path('user-request-details/', views.user_request_details, name='user_request_details'),
    path('forms/<int:pk>/', views.form_view, name='form_view'),

    path('user_form_view/<int:pk>/', views.user_form_view, name='user_form_view'),
    path('mis-report/', views.mis_report, name='mis_report'),
    
]
