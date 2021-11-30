from django.urls import path

from . import views

app_name = "pub"
urlpatterns = [
    path('', views.MensajesList.as_view(), name='MensajesList'),
    path('elim/', views.eliminar_sus, name='eliminar_sus'),
    path('sus/', views.suscripcion, name='suscripcion'),
]