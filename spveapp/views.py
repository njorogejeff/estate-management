from django.shortcuts import render, redirect
from .forms import OwnerForm, ResidentForm, StaffForm
from .models import HseOwner, Occupants, Staff


# Create your views here.
def index(request):
    return render(request, 'spveapp/index.html')


def owners_list(request):
    context = {'owners_list': HseOwner.objects.all()}
    return render(request, 'spveapp/houseowners_list.html', context)


def residents_list(request):
    context = {'residents_list': Occupants.objects.all()}
    return render(request, 'spveapp/residents_list.html', context)


def staff_list(request):
    context = {'staff_list': Staff.objects.all()}
    return render(request, 'spveapp/staff_list.html', context)


# Spring View Estate Registration Forms
def owner_form(request):
    if request.method == 'GET':
        oform = OwnerForm()
        return render(request, 'spveapp/houseowner_form.html', {'oform': oform})
    else:
        oform = OwnerForm(request.POST)
        if oform.is_valid():
            oform.save()
        return redirect('/houseowners')


def resident_form(request):
    if request.method == 'GET':
        rform = ResidentForm()
        return render(request, 'spveapp/resident_form.html', {'rform': rform})
    else:
        rform = ResidentForm(request.POST)
        if rform.is_valid():
            rform.save()
        return redirect('/residents')


def staff_form(request):
    if request.method == 'GET':
        sform = StaffForm()
        return render(request, 'spveapp/staff_form.html', {'sform': sform})
    else:
        sform = StaffForm(request.POST)
        if sform.is_valid():
            sform.save()
        return redirect('/staff')
