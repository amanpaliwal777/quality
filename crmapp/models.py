from django.db import models
from django.contrib.auth.models import User


# Create your models here.

class Clients(models.Model):
    superuser_id = models.ForeignKey(User, on_delete=models.CASCADE)
    client_name = models.CharField(max_length=100)
    client_business = models.CharField(max_length=200)
    client_phone = models.BigIntegerField()
    client_email = models.EmailField(max_length=100)
    client_address = models.CharField(max_length=300)
    client_country = models.CharField(max_length=20)
    client_work_description = models.CharField(max_length=300)
    client_created = models.DateTimeField()

    def __str__(self):
        return self.client_name


class Client_Response(models.Model):
    client_id = models.ForeignKey(Clients, on_delete=models.CASCADE)
    superuser_id = models.ForeignKey(User, on_delete=models.CASCADE)
    client_response = models.CharField(max_length=500)
    client_response_date = models.DateTimeField()


class Client_Services(models.Model):
    client_id = models.ForeignKey(Clients, on_delete=models.CASCADE)
    superuser_id = models.ForeignKey(User, on_delete=models.CASCADE)
    services = models.CharField(max_length=200)
    pricing = models.IntegerField()
    advance = models.IntegerField()
    due = models.IntegerField()
    quatation = models.FileField(upload_to='media', null=True)


class Invoice_Details(models.Model):
    client_id = models.ForeignKey(Clients, on_delete=models.CASCADE)
    GST = models.CharField(max_length=100)
    PAN = models.CharField(max_length=100)
