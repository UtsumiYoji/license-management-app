from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import License
from django.utils import timezone  # Use Django's timezone utilities

# Create your views here.

class LicenseValidationView(APIView):
    def get(self, request):
        license_key = request.query_params.get('license')
        if not license_key:
            return Response({"error": "License key is required."}, status=status.HTTP_400_BAD_REQUEST)
        
        try:
            license = License.objects.get(license_key=license_key)
            now = timezone.now()  # Use timezone-aware datetime
            is_valid = license.valid_until is None or license.valid_until > now
            return Response({
                "valid": is_valid,
                "until": license.valid_until,
                "body": license.body
            }, status=status.HTTP_200_OK)
        except License.DoesNotExist:
            return Response({"valid": False, "error": "License not found."}, status=status.HTTP_404_NOT_FOUND)
