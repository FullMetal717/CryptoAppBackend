from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager
from django.contrib.auth.models import PermissionsMixin
# Create your models here.

class UserManager(BaseUserManager):
    def create_user(self, username, email, password=None, **extra_fields):
        if not email:
            raise ValueError("The Email field must be set") 
        if not username:
            raise ValueError("The username field is required") 
        
        email = self.normalize_email(email) 
        user = self.model(username=username, email=email, **extra_fields) 
        user.set_password(password) 
        user.save(using=self._db)
        return user 
    
    def create_superuser(self, username, email, password=None, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True) 

        if extra_fields.get("is_staff") is not True:
            raise ValueError("is staff must be true for admin user")
        
        if extra_fields.get("is_superuser") is not True:
            raise ValueError("is superuser must be true for admin user")
        
        return self.create_user(username, email, password, **extra_fields) 
    
class User(AbstractBaseUser, PermissionsMixin):
    email = models.EmailField(unique=True, max_length=255)
    username = models.CharField(max_length=255, unique = True) 
    first_name = models.CharField(max_length=255, unique = True)
    last_name = models.CharField(max_length=255, unique = True)
    is_active = models.BooleanField(default= True)
    is_staff = models.BooleanField(default = False) 
    is_superuser = models.BooleanField(default = False) 

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username', 'first_name', 'last_name'] 

    objects = UserManager()

    def get_full_name(self):
        return f"{self.first_name} {self.last_name}" 
    
    def has_perm(self, perm, obj=None):
        return True
    
    def has_module_perms(self, app_label):
        return True 
    
    def __str__(self):
        return f"{self.first_name} | {self.email}" 