from django.urls import path
from . import views

urlpatterns = [
    path('', views.index),
    path('cadastro/', views.cadastro, name='cadastro'),
    path('update/<str:id>/', views.update, name='update'),
    #path('excluir/<str:id>/', views.excluir, name='excluir'),
 
]
