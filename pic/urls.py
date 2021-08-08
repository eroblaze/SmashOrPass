from django.urls import path
from . import views


urlpatterns = [
    path('', views.index, name='index'),
    path('smashes/', views.all_smashes),
    path('delete/<int:id>/', views.delete_id),
    path('deleteall/', views.delete_all),
]