# uploadphoto/views.py
from django.shortcuts import render, redirect
from .forms import PhotoForm

def uploadphoto_page(request):
    if request.method == 'POST':
        form = PhotoForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()  # Photo 객체가 DB에 저장되고, 파일은 MEDIA_ROOT/photos/에 저장됩니다.
            return redirect('uploadphoto_page')
    else:
        form = PhotoForm()
    return render(request, 'uploadphoto/uploadphoto.html', {'form': form})
