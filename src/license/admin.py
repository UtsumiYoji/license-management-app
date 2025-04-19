from django.contrib import admin
from .models import Application, Buyer, License, PaymentHistory


class LicenseAdmin(admin.ModelAdmin):
    readonly_fields = ('license_key', 'created_at', 'updated_at')
    

class PaymentHistoryAdmin(admin.ModelAdmin):
    readonly_fields = ('created_at', 'updated_at')    


# Register your models here.
admin.site.register(Application)
admin.site.register(Buyer)
admin.site.register(License, LicenseAdmin)
admin.site.register(PaymentHistory, PaymentHistoryAdmin)
