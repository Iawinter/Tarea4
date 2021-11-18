from django.urls import path

from . import views

app_name = "pub"
urlpatterns = [
    path('', views.index, name='index'),
    path('elim/', views.eliminar_sus, name='eliminar_sus'),
    path('sus/', views.suscripcion, name='suscripcion'),
]