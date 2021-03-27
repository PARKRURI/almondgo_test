from django.urls import path
from . import views


kakaopay_name ="kakaopay"

urlpatterns = [
    path('', views.index, name="index"),
    path('', views.approval, name="approval"),  
]
   