from django.db import models
from .validation import *
# Create your models here.

from django.db import models
from django.contrib.auth.models import (
    BaseUserManager, AbstractBaseUser
)
from django.conf import settings
from django.db.models.signals import post_save
from django.dispatch import receiver
from rest_framework.authtoken.models import Token
from datetime import datetime



class MyUserManager(BaseUserManager):
    def create_user(self, name, email, mobile, password=None):
        """
        Creates and saves a User with the given email, date of
        birth and password.
        """
        if not name:
            raise ValueError('Users must provide a name')

        if not email:
            raise ValueError('Users must have an email address')

        if not mobile:
            raise ValueError('Users must have a mobile number for password recovery')

        user = self.model(
            email=self.normalize_email(email),
            name=name,
            mobile= mobile
            
        )

        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, name, email, mobile, password=None):
        """
        Creates and saves a superuser with the given email, date of
        birth and password.
        """
        user = self.create_user(
            name=name,
            email=email,
            mobile=mobile,
            password=password,
        )
        user.is_admin = True
        user.save(using=self._db)
        return user


class MyUser(AbstractBaseUser):
    name = models.CharField(max_length=250,verbose_name='full name',help_text='Enter your full name',validators=[validate_name])
    email = models.EmailField(
        verbose_name='email address',
        max_length=255,
        unique=True,
        help_text='Enter your email address'
    )
    mobile = models.CharField(max_length=10,unique=True,verbose_name='mobile number',help_text='Please enter your mobile number without any prefix e.g. 1234567890',validators=[validate_mobile])
    is_active = models.BooleanField(default=True)
    is_admin = models.BooleanField(default=False)

    objects = MyUserManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['name','mobile']

    def __str__(self):
        return self.email

    def has_perm(self, perm, obj=None):
        "Does the user have a specific permission?"
        # Simplest possible answer: Yes, always
        return True

    def has_module_perms(self, app_label):
        "Does the user have permissions to view the app `app_label`?"
        # Simplest possible answer: Yes, always
        return True

    @property
    def is_staff(self):
        "Is the user a member of staff?"
        # Simplest possible answer: All admins are staff
        return self.is_admin




@receiver(post_save, sender=settings.AUTH_USER_MODEL)
def create_auth_token(sender, instance=None, created=False, **kwargs):
    if created:
        Token.objects.create(user=instance)


class Product(models.Model):
    prod_name = models.CharField(max_length=350,unique=True)
    type_choices = [
        ('clothing','Clothing'),
        ('bags','Bags & luggage'),
        ('footwear','Footwear'),
        ('electronics','Electronics'),
        ('beauty_grocery','Beauty & Grocery'),
        ('sports','Sports'),
        ('books','Books'),
        ('baby','Baby Products')
    ]
    prod_type = models.CharField(max_length=250,choices=type_choices,help_text="choose one from [clothing, bags, footwear, electronics, beauty_grocery, sports, books, baby]")
    prod_image = models.ImageField(upload_to='product_images/',blank=False, null=False)
    active = models.BooleanField(default=True)
    prod_desc = models.TextField(max_length=1500)
    prod_price = models.FloatField()
    updated_on = models.DateTimeField(default=datetime.now())
    created_on = models.DateTimeField(auto_now_add=True,editable=False)



    
