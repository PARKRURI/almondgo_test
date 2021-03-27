from django.db import models

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





