from django.db import models
from django.contrib.auth.models import (
    AbstractBaseUser,BaseUserManager
)
from django.utils.translation import ugettext_lazy as _

class UserManager(BaseUserManager):
    def create_user(self,email,username,password=None,location=None,is_active=True,is_staff=False,is_superuser=False):
        if not email:
            raise ValueError('users must have an emil address')
        
        if not username:
            raise ValueError('users must have an username address')
        
        if not password:
            raise ValueError('please write a strong password')
        
        user_obj = self.model(
            email=self.normalize_email(email),
            username = username,
            location = location
        )
        user_obj.set_password(password)
        user_obj.active=is_active
        user_obj.staff = is_staff
        user_obj.superuser = is_superuser
        user_obj.save(using=self._db)
        return user_obj
    
    def create_staffuser(self,email,username,location=None,password=None):
        user = self.create_user(
            email = email,
            username = username,
            password=password,
            location = location,
            is_staff = True
        )
        return user
    
    def create_superuser(self,email,username,location=None,password=None):
        user = self.create_user(
            email = email,
            username = username,
            password = password,
            location = location,
            is_staff = True,
            is_superuser = True

        )
        return user
    



class User(AbstractBaseUser):
    email = models.EmailField(max_length=255,unique=True,verbose_name=_('email address'))
    username = models.CharField(max_length=40,verbose_name=_('username'))
    location = models.CharField(max_length=255,verbose_name=_('location'),blank=True,null=True)
    active = models.BooleanField(default=True,verbose_name=_('is active'))
    staff = models.BooleanField(default=False,verbose_name=_('is staff'))
    superuser = models.BooleanField(default=False,verbose_name=_('is super user'))
    

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username']

    objects = UserManager()

    def __str__(self):
        return self.email
    
    def get_short_name(self):
        return self.email

    def has_perm(self,perm,obj=None):
        return True

    def has_module_perms(self,app_label):
        return True
        

    @property
    def is_active(self):
        return self.active
    
    @property
    def is_staff(self):
        return self.staff

    @property
    def is_superuser(self):
        return self.superuser







