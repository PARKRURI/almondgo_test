"""config URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path , include
from django.conf.urls import url #추가
# from almondgo.views import boardView
from almondgo.views import test
from almondgo.views import result
from almondgo.views import start
from almondgo.views import generalinfo
from almondgo.views import pick
from almondgo.views import service
from almondgo.views import findSentence
from almondgo.views import doSomething
from almondgo.views import firstpage
from almondgo.views import start2
from almondgo.views import fmain
from kakaopay.views import index
from kakaopay.views import approval
from almondgo.views import menupick
# from django.contrib import Product




urlpatterns = [
    path('admin/', admin.site.urls),
#    path('view/', boardView),
    path('', include ('blog.urls')),
    path('test/',test),
    path('search/', result),
    path('result/', result),
    path('start/', start),
    path('generalinfo/', generalinfo),
    path('pick/', pick),
    path('service/', doSomething),
    path('detail/', findSentence),
    path('firstpage/',firstpage),
    path('start2/',start2),
    path('fmain/', fmain),
    path('kakaopay/', index),
    path('approval/', approval),
    path('menupick/', menupick),
#    path('summernote/', include('djnago_summernote.urls')),
#    path('product_register/', ProductRegister),
   

]
   
               
