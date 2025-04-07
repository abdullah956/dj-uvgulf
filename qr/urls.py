from django.urls import path
from .views import add_certification, certification_list, generate_qr_code, certificate_details

urlpatterns = [
    path('add_certification/', add_certification, name='add_certification'),
    path('certifications/', certification_list, name='certification_list'),
    path('qr_code/<str:tac_number>/', generate_qr_code, name='generate_qr_code'),
    path('certificate/<str:tac_number>/', certificate_details, name='certificate_details'),  # New URL for certificate details
]
