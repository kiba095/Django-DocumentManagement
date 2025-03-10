from django.shortcuts import render,redirect
from .forms import UploadFileForm
from .models import MediaFile

# Create your views here.
def upload_file(request):
    if request.method == 'POST':
        form = UploadFileForm(request.POST,request.FILES)
        if form.is_valid():
            form.save()
            return redirect('upload_file')
    else:
        form = UploadFileForm()
    return render(request,'uploader/upload.html',{'form':form})


def file_list(request):
    files = UploadFileForm.objects.all()
    return render(request,'uploader/file_list.html',{'files':files})