from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class ProductModel(models.Model):
    title=models.CharField(max_length=200)
    image=models.ImageField(upload_to='images/', height_field=None, width_field=None)
    product_desc=models.TextField()
    timestamp=models.DateTimeField(auto_now_add=True)
    product_icon=models.ImageField(upload_to='images/')
    total_votes=models.IntegerField(default=0)
    url=models.TextField()
    hunter= models.ForeignKey(User, on_delete=models.CASCADE)
    
    def __str__(self):
        return self.title
    