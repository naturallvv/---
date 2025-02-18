# uploadphoto/admin.py
from django.contrib import admin
from .models import UserPhoto, ReferencePhoto

admin.site.register(UserPhoto)
admin.site.register(ReferencePhoto)