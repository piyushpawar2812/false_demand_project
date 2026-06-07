
from django.contrib import admin
from .models import RoleMaster, User


# =========================
# ROLE MASTER ADMIN
# =========================

@admin.register(RoleMaster)
class RoleMasterAdmin(admin.ModelAdmin):

    list_display = (
        'id',
        'role_name',
        'status',
        'is_deleted',
        'created_date',
    )

    search_fields = (
        'role_name',
    )

    list_filter = (
        'status',
        'is_deleted',
    )

    ordering = ('role_name',)

    readonly_fields = (
        'created_date',
        'updated_date',
    )

    fieldsets = (

        ("Role Information", {
            'fields': (
                'role_name',
            )
        }),

        ("Status Information", {
            'fields': (
                'status',
                'is_deleted',
            )
        }),

        ("Audit Information", {
            'fields': (
                'created_date',
                'updated_date',
            )
        }),
    )


# =========================
# USER ADMIN
# =========================

@admin.register(User)
class UserAdmin(admin.ModelAdmin):

    list_display = (
        'id',
        'login_id',
        'officer_name',
        'designation',
        'employee_no',
        'mobile_no',
        'role',
        'circle',
        'division',
        'status',
        'created_date',
    )

    search_fields = (
        'login_id',
        'officer_name',
        'designation',
        'employee_no',
        'mobile_no',
        'circle',
        'division',
    )

    list_filter = (
        'role',
        'status',
        'is_deleted',
        'circle',
        'division',
    )

    ordering = ('-id',)

    readonly_fields = (
        'created_date',
        'updated_date',
    )

    autocomplete_fields = ['role']

    fieldsets = (

        ("Login Credentials", {
            'fields': (
                'login_id',
                'password',
                'role',
            )
        }),

        ("Officer Information", {
            'fields': (
                'officer_name',
                'designation',
                'employee_no',
                'mobile_no',
            )
        }),

        ("Location Information", {
            'fields': (
                'circle',
                'division',
            )
        }),

        ("Status Information", {
            'fields': (
                'status',
                'is_deleted',
            )
        }),

        ("Audit Information", {
            'fields': (
                'created_date',
                'updated_date',
            )
        }),
    )

