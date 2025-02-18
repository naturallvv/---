# uploadphoto/models.py
from django.db import models

class Photo(models.Model):
    image = models.ImageField(upload_to='photos/')
    place_name = models.CharField(max_length=100)
    address = models.CharField(max_length=255, default='')
    uploaded_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Photo {self.id} - {self.place_name}"
