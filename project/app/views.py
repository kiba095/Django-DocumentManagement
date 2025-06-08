from django.shortcuts import render
from django.contrib.auth.decorators import login_required,user_passes_test
from .models import Notification,MediaFile
from django.contrib import messages
from django.shortcuts import get_object_or_404,redirect
from django.urls import reverse
from django.http import HttpResponse
from django.utils.html import escape 

#@login_required
def index(request):
    user = MediaFile.objects.all()
    return render(request,'app/index.html',{'index':user})

@login_required
def print_pdf_view(request, pk):
    obj = get_object_or_404(MediaFile, pk=pk)
    if not obj.filename.name.lower().endswith('.pdf'):
        return HttpResponse("Not a PDF",status =400)
    
    pdf_url = escape(obj.file.url)
    return HttpResponse(f"""
        <html>
        <head><title>PDF Viewer</title></head>
        <body style="margin:0">
            <iframe src="{pdf_url}" style="width:100%; height:100vh;" frameborder="0"></iframe>
            <script>
                document.addEventListener('DOMContentLoaded', function() {{
                    var iframe = document.querySelector('iframe');
                    iframe.onload = function() {{
                        iframe.contentWindow.print();
                    }};
                }});
            </script>                
        </body>
                        """)

@login_required
def notifications(request):
    user_notifications = Notification.objects.filter(recipient=request.user,is_read=False)
    return render(request,'notifications.html',{'notifications':user_notifications})

@login_required
def media_detail(request,detail_id):
    media_files = MediaFile.objects.filter(id=detail_id).first()
    return render(request,'app/media_detail.html',{'media':media_files})

#for the approver button
def is_approver(user):
    return user.groups.filter(name="admin_group").exists()

@login_required
@user_passes_test(is_approver)
def approve_document(request,doc_id):
    document = get_object_or_404(MediaFile,id=doc_id)
    document.status = 'approved'
    document.save()
    messages.success(request,"The Document has been approved successfully.")
    return redirect(reverse("admin:app_mediafile_changelist"))

@login_required
@user_passes_test(is_approver)
def reject_document(request,doc_id):
    document = get_object_or_404(MediaFile,id=doc_id)
    document.status = 'rejected'
    document.save()
    messages.error(request,"The Document has been rejected")
    return redirect(reverse("admin:app_mediafile_changelist"))