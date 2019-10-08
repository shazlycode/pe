from django.db import models
from django .utils import timezone

# Create your models here.

class DrugIndex(models.Model):
    trade_name=models.CharField(max_length=100, verbose_name='Trade Name')
    generic_name=models.CharField(max_length=100, verbose_name='Generic Name')
    uses=models.TextField(default='', verbose_name='Uses')
    dosage=models.TextField(default='', verbose_name='Dosage')
    image=models.TextField(default='',verbose_name='Image')
    
    def __str__(self):
        return self.generic_name
    
    class Meta:
        ordering=('-trade_name',)
        
        
class Post(models.Model):
    post_title= models.CharField(max_length=100, verbose_name='Subject')
    name= models.CharField(max_length=100, verbose_name='Name')
    email= models.EmailField(verbose_name='Email')
    post_body= models.TextField(default='',verbose_name='Message')
    date=models.DateTimeField(default=timezone.now)
    
    def __str__(self):
        return self.post_title
    
    class Meta:
        ordering= ('-date',)
