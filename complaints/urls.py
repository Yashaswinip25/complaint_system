from django.urls import path
from .views import submit_complaint, complaint_success,home

urlpatterns = [
    path('', home, name='home'),
    path('submit/', submit_complaint, name='submit_complaint'),
    path('success/', complaint_success, name='complaint_success'),
]
