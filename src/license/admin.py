from django.contrib import admin
from .models import Application, Buyer, License, PaymentHistory

# Register your models here.
admin.site.register(Application)
admin.site.register(Buyer)
admin.site.register(License)
admin.site.register(PaymentHistory)
