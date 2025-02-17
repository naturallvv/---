from django.shortcuts import render

def uploadphoto_page(request):
    return render(request, 'uploadphoto/uploadphoto.html')
