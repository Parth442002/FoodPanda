from django.db import models
from django.contrib.auth.models import AbstractUser
from django.conf import settings
from django.utils.translation import ugettext_lazy as _
from django.utils import timezone


class Address(models.Model):
    TYPES=(
        ('home',_('home')),
        ('office',_('office')),
        ('other',_('other'),)
    )
    address_type=models.CharField(choices=TYPES,max_length=10)
    street_address=models.TextField(max_length=200)
    pincode=models.PositiveIntegerField()
    city=models.CharField(max_length=200)
    state=models.CharField(max_length=50)
    
    def __str__(self):
        return self.street_address
    
    class Meta:
        verbose_name_plural='Addresses'

class Customer(AbstractUser):
    phone = models.CharField(max_length=10)
    GENDER_CHOICES=(
        ('M','Male'),
        ('F','Female'),
    )
    gender=models.CharField(max_length=10,choices=GENDER_CHOICES,null=True)
    date_of_birth = models.DateField(blank=True, null=True)
    address=models.ManyToManyField(Address,null=True)
    

    USERNAME_FIELD = 'username'
    REQUIRED_FIELDS = ['email', 'phone']