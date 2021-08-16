from django.urls import path
from . import views

app_name = 'main'

urlpatterns = [
    path('', views.index, name='index'),
    path('notebook/', views.NotebookPro.as_view(), name='notebook'),
    path('televizor/', views.TelevizorPro.as_view(), name='televizor'),
    path('konditsaner/', views.KonditsanerPro.as_view(), name='konditsaner'),
    path('smatphone/', views.SmartPhonePro.as_view(), name='smartphone'),
    path('gaz/', views.GazPro.as_view(), name='gaz')
]