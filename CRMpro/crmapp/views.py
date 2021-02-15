from django.shortcuts import render, HttpResponseRedirect, HttpResponse
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import authenticate, logout, login
from .models import Clients, Client_Response, Client_Services, Invoice_Details
from datetime import datetime
import os
from django.conf import settings
from django.shortcuts import Http404

dt = datetime.now()


# Create your views here.
def home(request):
    return HttpResponseRedirect('/login/')


def user_login(request):
    if not request.user.is_authenticated:
        if request.method == 'POST':
            forms = AuthenticationForm(request=request, data=request.POST)
            if forms.is_valid():
                uname = forms.cleaned_data['username']
                upass = forms.cleaned_data['password']
                user = authenticate(username=uname, password=upass)
                if user is not None:
                    login(request, user)
                    messages.success(request, 'login successfull!!!')
                    return HttpResponseRedirect('/profile/')
            return HttpResponse('form is invalid')

        else:
            forms = AuthenticationForm()
        return render(request, 'login.html', {'forms': forms})
    else:
        return render(request, 'profile.html', {'name': request.user})


def user_profile(request):
    if request.user.is_authenticated:
        responses = Client_Response.objects.filter(superuser_id=request.user.id)
        repotake = len(responses)
        context = {'name': request.user, 'repotake': repotake, 'responses': responses}
        return render(request, 'profile.html', context=context)
    else:
        return HttpResponseRedirect('/login/')


def user_logout(request):
    logout(request)
    return HttpResponseRedirect('/login/')


def clients_data(request):
    clients = Clients.objects.all()
    if request.method == 'POST':
        client_name = request.POST.get('client_name')
        client_business = request.POST.get('client_business')
        client_phone = request.POST.get('client_phone')
        client_email = request.POST.get('client_email')
        client_address = request.POST.get('client_address')
        client_country = request.POST.get('client_country')
        client_work_description = request.POST.get('client_work_description')
        data = Clients(client_name=client_name,
                       client_business=client_business,
                       superuser_id=User.objects.get(pk=request.user.id),
                       client_email=client_email,
                       client_phone=client_phone,
                       client_address=client_address,
                       client_country=client_country,
                       client_work_description=client_work_description,
                       client_created=dt)
        data.save()
        messages.success(request, 'Client added successfully !!!')
        return HttpResponseRedirect('/ClientsData/')
    else:
        return render(request, 'clients_data.html', {'name': request.user, 'clients': clients})


def clients_delete(request, id):
    if request.user.is_authenticated:
        if request.method == 'POST':
            cli = Clients.objects.get(pk=id)
            cli.delete()
            return HttpResponseRedirect('/ClientsData/')
        else:
            return HttpResponseRedirect('/ClientsData/')
    else:
        return HttpResponseRedirect('/login/')


def clients_edit(request, id):
    if request.method == 'POST':
        c = Clients.objects.get(pk=id)
        c.client_name = request.POST.get('client_name')
        c.client_business = request.POST.get('client_business')
        c.client_phone = request.POST.get('client_phone')
        c.client_email = request.POST.get('client_email')
        c.client_address = request.POST.get('client_address')
        c.client_country = request.POST.get('client_country')
        c.client_work_description = request.POST.get('client_work_description')
        c.save()
        return HttpResponseRedirect('/ClientsData/')
    else:
        client = Clients.objects.get(pk=id)
        return render(request, 'clients_data_edit.html', {'name': request.user, 'client': client})


def clients_profile(request, id):
    if request.user.is_authenticated:
        clirepo = Client_Response.objects.filter(client_id=id)
        cli_ser = Client_Services.objects.filter(client_id=id)
        invo = Invoice_Details.objects.filter(client_id=id)
        if request.method == 'POST':
            response = request.POST.get('response')

            data = Client_Response(
                client_id=Clients.objects.get(pk=id),
                superuser_id=User.objects.get(pk=request.user.id),
                client_response=response,
                client_response_date=dt,
            )
            data.save()
            return HttpResponseRedirect('/ClientProfile/{}'.format(id))

        else:
            client = Clients.objects.get(pk=id)
            return render(request, 'clients_profile.html',
                          {'name': request.user, 'client': client, 'clirepo': clirepo, 'cli_ser': cli_ser,'invo':invo})
    else:
        return HttpResponseRedirect('/')


def clients_service_add(request, id):
    if request.user.is_authenticated:
        if request.method == 'POST':
            service = request.POST.get('service')
            pricing = request.POST.get('pricing')
            advance = request.POST.get('advance')
            due = int(pricing) - int(advance)
            try:
                quatation = request.FILES['file']
            except:
                quatation = 'non'

            data = Client_Services(
                client_id=Clients.objects.get(pk=id),
                superuser_id=User.objects.get(pk=request.user.id),
                services=service,
                pricing=pricing,
                advance=advance,
                due=due,
                quatation=quatation
            )
            data.save()
            return HttpResponseRedirect('/ClientProfile/{}/'.format(id))

        else:
            return render(request, 'client_service_add.html', {'name': request.user, 'cli_id': id})
    else:
        return HttpResponseRedirect('/login/')


def clients_service_edit(request, id):
    if request.user.is_authenticated:
        cli_ser = Client_Services.objects.get(pk=id)
        if request.method == 'POST':
            c = Client_Services.objects.get(pk=id)
            c.services = request.POST.get('service')
            pricing = request.POST.get('pricing')
            advance = request.POST.get('advance')
            c.pricing = pricing
            c.advance = advance
            c.due = int(pricing) - int(advance)
            try:
                c.quatation = request.FILES['file']
            except:
                c.quatation = 'non'

            c.save()

            return HttpResponseRedirect('/ClientProfile/{}/'.format(c.client_id.id))
        else:
            return render(request, 'client_service_edit.html', {'name': request.user, 'cli_id': id, 'cli_ser': cli_ser})
    else:
        return HttpResponseRedirect('/login/')


def clients_service_delete(request, id):
    if request.user.is_authenticated:
        if request.method == 'POST':
            c = Client_Services.objects.get(pk=id)
            id = c.client_id.id
            c.delete()

            return HttpResponseRedirect('/ClientProfile/{}/'.format(id))
        else:
            return HttpResponseRedirect('/ClientProfile/{}/'.format(id))


def download(request, path):
    file_path = os.path.join(settings.MEDIA_ROOT, path)
    if os.path.exists(file_path):
        with open(file_path, 'rb') as fh:
            response = HttpResponse(fh.read(), content_type='application/quatation')
            response['Content-Disposition'] = 'inline;filename=' + os.path.basename(file_path)
            return response
    raise Http404


def clients_invoice(request, id):
    if request.user.is_authenticated:
        dt = datetime.now()
        pricing = 0
        due = 0
        advance = 0
        cli_ser = Client_Services.objects.filter(client_id=id)
        client = Clients.objects.get(pk=id)
        invo = Invoice_Details.objects.filter(client_id=id)
        for c in cli_ser:
            pricing += c.pricing
            due += c.due
            advance += c.advance

        if request.method == 'POST':

            context = {'advance': advance, 'due': due, 'pricing': pricing,
                       'name': request.user, 'cli_id': id, 'cli_ser': cli_ser,
                       'client': client, 'dt': dt,'invo':invo}
            return render(request, 'invoice.html', context=context)

        else:
            return HttpResponseRedirect('/')
    else:
        return HttpResponseRedirect('/')


def gst_add(request, id):
    if request.user.is_authenticated:
        cli = Invoice_Details.objects.filter(client_id=id).count()

        if cli ==0:
            if request.method == 'POST':
                GST = request.POST.get('GST')
                PAN = request.POST.get('PAN')

                data = Invoice_Details(
                    client_id=Clients.objects.get(pk=id),
                    GST=GST,
                    PAN=PAN,
                )
                data.save()
                return HttpResponseRedirect('/ClientProfile/{}/'.format(id))

            else:
                return render(request, 'client_gst_add.html', {'name': request.user, 'cli_id': id})
        else:
            return HttpResponseRedirect('/login/')
    else:
        return HttpResponseRedirect('/login/')


def gst_delete(request, id):
    if request.user.is_authenticated:
        if request.method == 'POST':
            c = Invoice_Details.objects.get(client_id=id)

            c.delete()

            return HttpResponseRedirect('/ClientProfile/{}/'.format(id))
        else:
            return HttpResponseRedirect('/ClientProfile/{}/'.format(id))
