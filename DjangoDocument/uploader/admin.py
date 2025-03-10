from django.contrib import admin
from django.urls import path
from django.template.response import TemplateResponse
from django.contrib import admin
from .models import MediaFile,Notification
from django.shortcuts import render,get_object_or_404
from django.utils.html import format_html
from django.urls import reverse 
from django.contrib.admin.sites import site

def custom_admin_view(request,obj_id):

    if not request.user.is_active or not request.user.is_staff:
        return admin.site.login(request)

    media = get_object_or_404(MediaFile,id=obj_id)
    context = {
        **site.each_context(request),
        'title': f'Custom Page - {media.id}',
        'media': media,

    }
    return render(request,'admin/custom_page.html',context)

#Extend Django Admin Urls
class CustomAdmin(admin.ModelAdmin):

    list_display = ("title","status_with_tooltip","user","media_type","uploaded_at","custom_page_link")

    def custom_page_link(self,obj):
        url = reverse("admin:custom_page",args=[obj.id])
        return format_html('<a href="{}" class="button">Demo_View</a>',url)
    custom_page_link.short_description = "Custom Pages"

    def status_with_tooltip(self,obj):
        return format_html(f'<span title="{obj.remarks}">{obj.status}</span>')


    def get_urls(self):
        urls = super().get_urls()
        custom_urls = [
            path('custom-page/<int:obj_id>/',custom_admin_view,name='custom_page')
        ]
        return custom_urls + urls



admin.site.register(MediaFile,CustomAdmin)
admin.site.register(Notification)