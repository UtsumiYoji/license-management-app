from django.urls import path
from .views import LicenseValidationView

urlpatterns = [
    path('', LicenseValidationView.as_view(), name='license-validation'),
]