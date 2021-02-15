from django.urls import path
from . import views
from django.conf.urls.static import static
from django.conf import settings
from django.conf.urls import url
from django.views.static import serve

urlpatterns = [
                  path('', views.home, name='home'),
                  path('login/', views.user_login, name='login'),
                  path('profile/', views.user_profile, name='profile'),
                  path('logout/', views.user_logout, name='logout'),
                  path('ClientsData/', views.clients_data, name='clients_data'),
                  path('ClientDelete/<int:id>/', views.clients_delete, name='ClientDelete'),
                  path('ClientEdit/<int:id>/', views.clients_edit, name='ClientEdit'),
                  path('ClientAllRepo/', views.clients_edit, name='allrepo'),
                  path('ClientProfile/<int:id>/', views.clients_profile, name='ClientProfile'),
                  path('ClientServicesA/<int:id>/', views.clients_service_add, name='ClientServicesA'),
                  path('ClientServicesE/<int:id>/', views.clients_service_edit, name='ClientServicesE'),
                  path('ClientServicesD/<int:id>/', views.clients_service_delete, name='ClientServicesD'),
                  path('invoice/<int:id>/', views.clients_invoice, name='invoice'),
                  path('gst_add/<int:id>/', views.gst_add, name='gst_add'),
                  path('gst_delete/<int:id>/', views.gst_delete, name='gst_delete'),
                  url(r'^download/(?P<path>.*)$', serve, {'document_root': settings.MEDIA_ROOT})
              ] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
