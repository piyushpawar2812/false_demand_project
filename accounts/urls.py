
from django.urls import path
from .views import login_view, dashboard,logout_view,dashboard_officer

urlpatterns = [
    path('', login_view, name='login'),
    path('dashboard/', dashboard, name='dashboard'),
    path('dashboard_officer/', dashboard_officer, name='dashboard_officer'),
    path('logout/', logout_view, name='logout'),
    
    
]
