from django.db import models

# Create your models here.
class Neighbourhood(models.Model):
    mtaani_name = models.CharField(max_length=30, null=True)
    mtaani_location = models.CharField(max_length=30, null=True)
    mtaani_occupants = models.PositiveIntegerField(null=True)

class Profile(models.Model):
    neighbourhood = models.ForeignKey(Neighbourhood, null=True, on_delete=models.CASCADE)

class Post(models.Model):
    post_image = models.ImageField(upload_to = 'posts/', null=True)
    post_description = models.TextField(null=True)
    profile_user = models.ForeignKey(Profile, null=True, on_delete=models.CASCADE)
    neighbourhood = models.ForeignKey(Neighbourhood, null=True, on_delete=models.CASCADE)

class Business(models.Model):
    business_name = models.CharField(max_length=30, null=True)
    business_email = models.EmailField(null=True)
    neighbourhood = models.ForeignKey(Neighbourhood,null=True, on_delete=models.CASCADE)

class Contact(models.Model):
    police_contact = models.CharField(null=True, max_length=30)
    hospital_contact = models.CharField(null=True, max_length=30)
    neighbourhood = models.ForeignKey(Neighbourhood, null=True, on_delete=models.CASCADE)