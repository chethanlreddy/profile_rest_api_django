from django.db import models
from django.contrib.auth.models import AbstractBaseUser
from django.contrib.auth.models import PermissionsMixin

class UserProfile(AbstractBaseUser,PermissionsMixin):
    '''Databse model for users in the system'''
    email = models.EmailField(max_length=255, unique=True)
    name = models.CharField(max_length=255)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default = False)
    
    objects = UserProfileManager()

    USERNAME_FIELD  = "email"
    REQUIRED_FIELDS = ['name']

    def get_full_name(self):
        '''Retrives full name'''
        return self.name
    
    def get_short_name(self):
        '''Retrives short name'''
        return self.name
    
    def __str__(self):
        '''Returns string representation of the user'''
        return self.email

# Create your models here.
