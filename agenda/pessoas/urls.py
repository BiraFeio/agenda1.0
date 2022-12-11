from django.urls import path
from . import views

urlpatterns = [
    path('',views.index,name="index"),
    path('inserir/',views.inserir,name='inserir'),
    path('inserir/registrar/',views.registrar,name='registrar'),
    path('delete/<int:id>',views.delete,name='delete'),
]