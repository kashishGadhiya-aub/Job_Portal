from django.urls import path
from . import views

urlpatterns = [
    path('edit/', views.edit_company, name='edit_company'),
    path('register/', views.register_company, name='register_company'),
    path('dashboard/', views.company_dashboard, name='company_dashboard'),
]
