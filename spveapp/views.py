from django.shortcuts import render
from .forms import HseOwnerForm, ResidentForm, StaffForm


# Create your views here.
def hseowners_list(request):
    return render(request, 'spveapp/hseowners_list.html')


def residents_list(request):
    return render(request, 'spveapp/residents_list.html')


def staff_list(request):
    return render(request, 'spveapp/staff_list.html')


# Spring View Estate Registration Forms
def hseowner_form(request):
    hseowner = HseOwnerForm()
    return render(request, 'spveapp/hseowner_form.html', {'hseowner': hseowner})


def residents_form(request):
    residents = ResidentForm()
    return render(request, 'spveapp/residents_form.html', {'residents': residents})


def staff_form(request):
    staff = StaffForm()
    return render(request, 'spveapp/staff_form.html', {'staff': staff})
