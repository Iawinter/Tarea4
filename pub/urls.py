from django.urls import path

from . import views

app_name = "pub"
urlpatterns = [
    path('', views.suscripcion, name='suscripcion'),
    path('elim/', views.eliminar_sus, name='eliminar_sus'),
]