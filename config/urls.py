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
from almondgo.views import cartcart
from almondgo.views import near
from almondgo.views import korea
from almondgo.views import china
from almondgo.views import cafe
from almondgo.views import gwang
from almondgo.views import quai
from almondgo.views import ame
from almondgo.views import ameshort
from almondgo.views import amelong
from almondgo.views import ameall
from almondgo.views import amesub
from almondgo.views import jja
from almondgo.views import jjashort
from almondgo.views import jjalong
from almondgo.views import jjasub
from almondgo.views import jjapay1
from almondgo.views import jjapay3
from almondgo.views import pay1
from almondgo.views import pay2
from almondgo.views import pay3
from almondgo.views import gwangoff
from almondgo.views import quaioff
from almondgo.views import dduckoff
from almondgo.views import boshort
from almondgo.views import bolong
from almondgo.views import bosub
from almondgo.views import boall
from almondgo.views import bo
from almondgo.views import dduck
from almondgo.views import menupick
from almondgo.views import jjaall
from almondgo.views import bopay1
from almondgo.views import bopay2
from almondgo.views import bopay3
from almondgo.views import amepay1
from almondgo.views import amepay2
from almondgo.views import amepay3

# from almondgo.views import booff

# from django.contrib import Product




urlpatterns = [
    path('admin/', admin.site.urls),
#    path('view/', boardView),
#   path('', include ('blog.urls')),
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
    path('cartcart/', cartcart),
    path('near/', near),
    path('korea/', korea),
    path('china/', china),
    path('cafe/',cafe),
    path('pay1/', pay1),
    path('pay2/', pay2),
    path('pay3/', pay3),
    path('gwang/', gwang),
    path('ame/', ame),
    path('ameshort/', ameshort),
    path('amelong/', amelong),
    path('amesub/', amesub),
    path('ameall/', ameall),
    path('quai/', quai),
    path('jja/', jja),
    path('jjashort/', jjashort),
    path('jjalong/', jjalong),
    path('jjasub/', jjasub),
    path('jjaall/', jjaall),
    path('jjapay1/', jjapay1),
    path('gwangoff/', gwangoff),
    path('quaioff/', quaioff),
    path('dduckoff/', dduckoff),
#     path('booff/', booff),
    path('boshort/', boshort),
    path('bolong/', bolong),
    path('bosub/', bosub),
    path('boall/', boall),
    path('bo/', bo),
    path('dduck/', dduck),
    path('bopay1/', bopay1),
    path('bopay2/', bopay2),
    path('bopay3/', bopay3),
    path('amepay1/', amepay1),
    path('amepay2/', amepay2),
    path('amepay3/', amepay3),

]


#    path('summernote/', include('djnago_summernote.urls')),
#    path('product_register/', ProductRegister),
   


   
               
