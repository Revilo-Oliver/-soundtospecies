from django.db import models
from django.conf import settings

# Create your models here.
class App_user(models.Model):
    User_ID = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    name = models.CharField(max_length=255)
    email = models.CharField(max_length=255)
    latitude = models.CharField(max_length=255)
    longitude = models.CharField(max_length=255)
    phone = models.CharField(max_length=255)

class Species(models.Model):
    species_ID = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    name = models.CharField(max_length=255)
    catagory = models.CharField(max_length=255)
    threat_level = models.CharField(max_length=255)
    image= models.CharField(max_length=255)
    sound_file = models.CharField(max_length=255)

class Voice_record(models.Model):
    user_id = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    audio_file = models.CharField(max_length=255)
    latitude = models.CharField(max_length=255)
    longitude = models.CharField(max_length=255)

class Zone(models.Model):
    voice_id = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    zone_type = models.CharField(max_length=255)
    identified_species_id = models.CharField(max_length=255)

class News(models.Model):
    news_id = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    title = models.CharField(max_length=255)
    content = models.CharField(max_length=255)
    image = models.CharField(max_length=255)
    date = models.CharField(max_length=255)

class Downloads(models.Model):
    downloads_id = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    user_id = models.CharField(max_length=255)
    sound_id = models.CharField(max_length=255)
    date = models.CharField(max_length=255)
