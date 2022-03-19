from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Neighbourhood(models.Model):
    mtaani_name = models.CharField(max_length=30, null=True)
    mtaani_location = models.CharField(max_length=30, null=True)
    mtaani_occupants = models.PositiveIntegerField(null=True)

    def __str__(self):
        return self.mtaani_name

class Profile(models.Model):
    user = models.OneToOneField(User, null=True, on_delete=models.CASCADE)
    neighbourhood = models.ForeignKey(Neighbourhood, null=True, on_delete=models.CASCADE)

    def __str__(self):
        return self.user.username

class Post(models.Model):
    post_image = models.ImageField(upload_to = 'posts/', null=True)
    post_name = models.CharField(max_length=30, null=True)
    post_description = models.TextField(null=True)
    profile_user = models.ForeignKey(Profile, null=True, on_delete=models.CASCADE)
    neighbourhood = models.ForeignKey(Neighbourhood, null=True, on_delete=models.CASCADE)

    def __str__(self):
        return self.post_name

class Business(models.Model):
    business_name = models.CharField(max_length=30, null=True)
    business_email = models.EmailField(null=True)
    neighbourhood = models.ForeignKey(Neighbourhood,null=True, on_delete=models.CASCADE)

    def __str__(self):
        return self.business_name

class Contact(models.Model):
    police_contact = models.CharField(null=True, max_length=30)
    hospital_contact = models.CharField(null=True, max_length=30)
    neighbourhood = models.ForeignKey(Neighbourhood, null=True, on_delete=models.CASCADE)

    def __str__(self):
        return self.police_contact