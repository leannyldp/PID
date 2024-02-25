from django.urls import path 
from . import views


urlpatterns = [
    path('', views.home),
    path('trabajador', views.index, name='trabajador'),
    path('trabajador/add',views.add, name='trabajador-add'),
    path('trabajador/edit/<int:pk>', views.edit, name='trabajador-edit'),
    path('trabajador/delete/<int:pk>', views.delete, name='trabajador-delete'),
   
]

