from django.db.models import Sum
from django.shortcuts import render

# Create your views here.
# In views.py
from django.http import HttpResponse
from django.conf import settings
import os

from django.views import View

from myapp.models import Institution, Donation


class LandingPage(View):
    def get(self, request):
        total_bags = Donation.objects.all().aggregate(Sum('quantity'))['quantity__sum']
        total_organizations = Institution.objects.count()
        fundations = Institution.objects.filter(type='fundacja')
        NGOs = Institution.objects.filter(type='organizacja_pozarzadowa')
        local_collections = Institution.objects.filter(type='zbiorka_lokalna')
        return render(request, 'index.html', {
            'total_bags': total_bags,
            'total_organizations': total_organizations,
            'fundations': fundations,
            'NGOs': NGOs,
            'local_collections': local_collections
        })



class AddDonation(View):

    def get(self, request):
        return render(request, 'form.html')


class Login(View):
    def get(self, request):
        return render(request, 'login.html')

class Register(View):
    def get(self, request):
        return render(request, 'register.html')