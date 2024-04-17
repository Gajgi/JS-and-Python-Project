from django.contrib.auth.models import User
from django.db import models

# Create your models here.
class Category(models.Model):
    name = models.CharField(max_length=100)


class Institution(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    INSTITUTION_TYPE_CHOICES = [
        ('fundacja', 'Fundacja'),
        ('organizacja_pozarzadowa', 'Organizacja pozarządowa'),
        ('zbiorka_lokalna', 'Zbiórka lokalna'),
    ]
    type = models.CharField(max_length=100, choices=INSTITUTION_TYPE_CHOICES, default='fundacja')
    categories = models.ManyToManyField('Category', related_name='institutions')



class Donation(models.Model):
    # Atrybuty modelu Donation
    quantity = models.PositiveIntegerField()
    categories = models.ManyToManyField('Category', related_name='donations')
    institution = models.ForeignKey(Institution, on_delete=models.CASCADE)
    address = models.CharField(max_length=100)
    phone_number = models.CharField(max_length=20)
    city = models.CharField(max_length=50)
    zip_code = models.CharField(max_length=10)
    pick_up_date = models.DateField()
    pick_up_time = models.TimeField()
    pick_up_comment = models.TextField()
    user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)

