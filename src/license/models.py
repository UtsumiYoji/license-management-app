import uuid
from django.db import models


# Create your models here.
class Application(models.Model):
    name = models.CharField(max_length=255, null=False, blank=False)

    def __str__(self):
        return self.name


class Buyer(models.Model):
    name = models.CharField(max_length=255, null=False, blank=False)
    email = models.EmailField(null=False, blank=False)
    note = models.TextField(null=True, blank=True)  # Optional field for any additional notes
    created_at = models.DateTimeField(auto_now_add=True, null=False, blank=False)

    def __str__(self):
        return self.name


class License(models.Model):
    application_object = models.ForeignKey(Application, on_delete=models.CASCADE, related_name='licenses')
    buyer_object = models.ForeignKey(Buyer, on_delete=models.CASCADE, related_name='licenses')
    
    license_key = models.CharField(max_length=255, null=False, blank=False, unique=True, default=uuid.uuid4)
    valid_until = models.DateTimeField(null=True, blank=True)
    body = models.JSONField(null=True, blank=True)

    created_at = models.DateTimeField(auto_now_add=True, null=False, blank=False)
    updated_at = models.DateTimeField(auto_now=True, null=False, blank=False)
    
    def __str__(self):
        return f"{self.application_object.name} - {self.buyer_object.name} until {self.valid_until}"


class PaymentHistory(models.Model):
    license_object = models.ForeignKey(License, on_delete=models.CASCADE, related_name='payment_history')
    amount = models.PositiveIntegerField(null=False, blank=False)
    note = models.TextField(null=True, blank=True)  # Optional field for any additional notes
    paid_at = models.DateTimeField(null=False, blank=False)
    created_at = models.DateTimeField(auto_now_add=True, null=False, blank=False)
    
    def __str__(self):
        return f"Payment of {self.amount} by {self.license_object.buyer_object.name} for {self.license_object.application_object.name}"
