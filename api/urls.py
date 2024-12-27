from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('api/medicaments', views.medicaments, name='medicaments'),
    path('api/verifierordonnance', views.verifier_ordonnance, name='verifier_ordonnance'),
]