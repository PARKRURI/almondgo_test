from django.db import models
# from shop.models import Product

# Create your models here.

def create_user(self,email,password, **kwargs):
    kwargs.setdefault('is_admin', True)
    kwargs.setdefault('is_staff', True)
    kwargs.setdefault('is_superuser', True)


class Board(models.Model):
    title = models.CharField(max_length=30)
    content_type = models.CharField(max_length=20)
    content = models.TextField()
    write_date = models.DateTimeField(auto_now_add=True)
'''
# 상품등록
class Product(models.Model):
    name = models.CharField(max_length =32, verbose_name="상품명")
    price = models.IntegerField(verbose_name="상품 가격")
    description = models.TextField(verbose_name="상품 설명")

    def __str__(self):
        return self.name

    class Meta:
        db_table ="Shoppingmall_Product"
        verbose_name ="상품"
        verbose_name_plural = "상품"

'''
'''
#cart 관련 모델 생성 
class Cart(models.Model):
    cart_id = models.CharField(max_length=250, blank=True)
    date_added = models.DateField(auto_now_add=True)
    class Meta:
        db_table = 'Cart'
        ordering = ['date_added']

    def __str__(self):
        return self.cart_id

class CartItem(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    cart = models.ForeignKey(Cart, on_delete=models.CASCADE)
    quantity = models.IntegerField()
    active = models.BooleanField(default=True)
    class Meta:
        db_table = 'CartItem'

    def sub_total(self):
        return self.product.price * self.quantity

    def __str__(self):
        return self.product

'''