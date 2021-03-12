from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.hseowners_list),
    path('residents/', views.residents_list),
    path('staff/', views.staff_list),
    path('houseownerregistrationform/', views.hseowner_form),
    path('residentregistrationform/', views.residents_form),
    path('staffregistrationform/', views.staff_form),

]
