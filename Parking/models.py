from django.db import models
from django.contrib.auth.models import User


class record(models.Model):
    created_at = models.DateTimeField(auto_created= True)
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    date_of_birth = models.DateField()
    email = models.EmailField(max_length=254)
    phone_number = models.CharField(max_length=10)
    address = models.CharField(max_length=100)
    zipcode = models.CharField(max_length = 50)
    city = models.CharField(max_length=254)
    state =models.CharField(max_length=254)
    
    
    def __str__(self):
        return (f"{self.created_at }{self.first_name} {self.last_name} {self.date_of_birth} {self.email} ")
        
    class ProfileForm(models.Model):
        user = models.OneToOneField(User, on_delete=models.CASCADE)
        bio = models.TextField(blank=True)
        

    def __str__(self):
        return f'Profile of {self.user.username}'

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    # Add other fields related to the profile, for example:
    bio = models.TextField(blank=True)
    location = models.CharField(max_length=100, blank=True)
    # Add any other fields you need

    def __str__(self):
        return self.user.username + "'s Profile"
