from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('houseownerregistrationform/', views.owner_form, name='owner_reg'),
    path('residentregistrationform/', views.resident_form, name='resident_reg'),
    path('staffregistrationform/', views.staff_form, name='staff_reg'),
    path('<int:hseownerid>/', views.owner_form, name='owner_update'),
    path('<int:residentid>/', views.resident_form, name='resident_update'),
    path('<int:staffid>/', views.staff_form, name='staff_update'),
    path('houseowners/', views.owners_list, name='owners_list'),
    path('residents/', views.residents_list, name='residents_list'),
    path('staff/', views.staff_list, name='staff_list'),
]
