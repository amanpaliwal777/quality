from django.contrib import admin
# Register your models here.
from .models import Clients, Client_Response, Client_Services, Invoice_Details


@admin.register(Clients)
class AdminClient(admin.ModelAdmin):
    list_display = ['client_name', 'client_business', 'client_phone', 'client_address', 'client_country',
                    'client_work_description']


@admin.register(Client_Response)
class AdminClientResponse(admin.ModelAdmin):
    list_display = ['client_id', 'superuser_id', 'client_response', 'client_response_date']


@admin.register(Client_Services)
class AdminClientServices(admin.ModelAdmin):
    list_display = ['client_id', 'superuser_id', 'services', 'pricing', 'advance', 'due',
                    'quatation']


@admin.register(Invoice_Details)
class AdminInvoiceDetails(admin.ModelAdmin):
    list_display = ['client_id', 'GST', 'PAN']
