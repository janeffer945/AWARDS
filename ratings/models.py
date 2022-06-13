from django.db import models
from cloudinary.models import CloudinaryField
from django.contrib.auth.models import User

from django.db import models



# Create your models here.
class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    profile_photo = CloudinaryField('image')
    bio = models.CharField(max_length=500, blank=True, null=True)
    contact = models.CharField(max_length=50, blank=True, null=True)
