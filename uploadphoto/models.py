# uploadphoto/models.py
from django.db import models

# 사용자가 업로드한 사진 정보를 저장하는 모델
class UserPhoto(models.Model):
    image = models.ImageField(upload_to='user_photos/')
    place_name = models.CharField(max_length=100,blank=True,null=True)
    address = models.CharField(max_length=255,blank=True,null=True)
    uploaded_at = models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return f"UserPhoto {self.id} - {self.place_name}"

# 우리가 직접 넣는(라벨링된) 사진 정보를 저장하는 모델
class ReferencePhoto(models.Model):
    image = models.ImageField(upload_to='reference_photos/')
    place_name = models.CharField(max_length=100)
    address = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"ReferencePhoto {self.id} - {self.place_name}"
