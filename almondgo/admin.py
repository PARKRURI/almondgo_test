from django.contrib import admin
from .models import Board
# from .models import Product

# Register your models here.

admin.site.register(Board)

'''
#상품 등록
class ProductAdmin(admin.ModelAdmin):
    list_display = ('name','price',)
'''
