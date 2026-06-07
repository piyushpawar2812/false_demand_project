
from django.contrib import admin
from .models import FalseDemandRequest, LocationDetails
from django.utils.html import format_html


@admin.register(FalseDemandRequest)
class FalseDemandRequestAdmin(admin.ModelAdmin):

    list_display = (
        'id',
        'name',
        'mobile',
        'consumer_no',
        'requested_amount',
        'circle_id',
        'division_id',
        'cgm_status',
        'ao_status',
        'gm_status',
        'final_puss_status',
        'created_document'
    )

    search_fields = (
        'name',
        'mobile',
        'consumer_no',
        'location_code',
        'circle_id',
        'division_id'
    )

    list_filter = (
        'cgm_status',
        'ao_status',
        'dgm_onm_status',
        'dgm_vig_status',
        'gm_status',
        'zonal_officer_status',
        'final_puss_status',
        'state',
        'city'
    )

    ordering = ('-id',)

    readonly_fields = (
        'document_preview',
        'cgm_doc_preview',
        'ao_doc_preview',
        'dgm_onm_doc_preview',
        'dgm_vig_doc_preview',
        'gm_doc_preview',
        'zonal_doc_preview',
    )

    fieldsets = (

        ("Consumer Information", {
            'fields': (
                'name',
                'mobile',
                'address',
                'city',
                'state',
                'consumer_no',
                'request_id',
                'requested_amount',
                'terrif_code',
            )
        }),

        ("Location Information", {
            'fields': (
                'location_code',
                'circle_id',
                'division_id',
            )
        }),

        ("Main Document", {
            'fields': (
                'document',
                'document_preview',
            )
        }),

        ("CGM Section", {
            'fields': (
                'cgm_status',
                'cgm_remark',
                'cgm_date_time',
                'cgm_doc',
                'cgm_doc_preview',
                'cgm_name_mobile',
            )
        }),

        ("AO Section", {
            'fields': (
                'ao_status',
                'ao_remark',
                'ao_date_time',
                'ao_doc',
                'ao_doc_preview',
                'ao_name_mobile',
            )
        }),

        ("DGM ONM Section", {
            'fields': (
                'dgm_onm_status',
                'dgm_onm_remark',
                'dgm_onm_date_time',
                'dgm_onm_doc',
                'dgm_onm_doc_preview',
                'dgm_onm_name_mobile',
            )
        }),

        ("DGM Vigilance Section", {
            'fields': (
                'dgm_vig_status',
                'dgm_vig_remark',
                'dgm_vig_date_time',
                'dgm_vig_doc',
                'dgm_vig_doc_preview',
                'dgm_vig_name_mobile',
            )
        }),

        ("GM Section", {
            'fields': (
                'gm_status',
                'gm_remark',
                'gm_date_time',
                'gm_doc',
                'gm_doc_preview',
                'gm_name_mobile',
            )
        }),

        ("Zonal Officer Section", {
            'fields': (
                'zonal_officer_status',
                'zonal_officer_remark',
                'zonal_officer_date_time',
                'zonal_officer_doc',
                'zonal_doc_preview',
                'zonal_officer_name_mobile',
                'final_puss_status',
            )
        }),
    )

    # ==========================
    # FILE PREVIEW METHODS
    # ==========================

    def document_preview(self, obj):
        if obj.document:
            return format_html(
                "<a href='{}' target='_blank'>View Document</a>",
                obj.document.url
            )
        return "No File"

    def cgm_doc_preview(self, obj):
        if obj.cgm_doc:
            return format_html(
                "<a href='{}' target='_blank'>View CGM File</a>",
                obj.cgm_doc.url
            )
        return "No File"

    def ao_doc_preview(self, obj):
        if obj.ao_doc:
            return format_html(
                "<a href='{}' target='_blank'>View AO File</a>",
                obj.ao_doc.url
            )
        return "No File"

    def dgm_onm_doc_preview(self, obj):
        if obj.dgm_onm_doc:
            return format_html(
                "<a href='{}' target='_blank'>View DGM ONM File</a>",
                obj.dgm_onm_doc.url
            )
        return "No File"

    def dgm_vig_doc_preview(self, obj):
        if obj.dgm_vig_doc:
            return format_html(
                "<a href='{}' target='_blank'>View DGM VIG File</a>",
                obj.dgm_vig_doc.url
            )
        return "No File"

    def gm_doc_preview(self, obj):
        if obj.gm_doc:
            return format_html(
                "<a href='{}' target='_blank'>View GM File</a>",
                obj.gm_doc.url
            )
        return "No File"

    def zonal_doc_preview(self, obj):
        if obj.zonal_officer_doc:
            return format_html(
                "<a href='{}' target='_blank'>View Zonal File</a>",
                obj.zonal_officer_doc.url
            )
        return "No File"

    def created_document(self, obj):
        if obj.document:
            return "Uploaded"
        return "No File"

    created_document.short_description = "Main Doc"


@admin.register(LocationDetails)
class LocationDetailsAdmin(admin.ModelAdmin):

    list_display = (
        'id',
        'circle_name',
        'division_name',
        'zone_name',
        'circle_id',
        'division_id',
        'code',
        'short_code',
        'phone_no'
    )

    search_fields = (
        'circle_name',
        'division_name',
        'zone_name',
        'short_code',
        'phone_no'
    )

    list_filter = (
        'circle_name',
        'zone_name'
    )

    ordering = ('circle_name',)

