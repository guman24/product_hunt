from django.shortcuts import render,redirect
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from products.models import ProductModel
from django.utils import timezone

# Create your views here.

def home(request):
    return render(request,'product/home.html')

@login_required
def create(request):
    if request.method=="POST":
        if request.POST['title'] and request.POST['product_desc'] and request.FILES['product_image'] and request.FILES['product_icon'] and request.POST['product_url']:
            product=ProductModel()
            product.title=request.POST['title']
            product.product_desc=request.POST['product_desc']
            product.image=request.FILES['product_image']
            product.icon=request.FILES['product_icon']
            if request.POST['product_url'].startswith('https://') or request.POST['product_url'].startswith('http://'):
                product.url=request.POST['product_url']
            else:
                product.url="http://"+request.POST['product_url']
            product.timestamp=timezone.datetime.now()
            product.hunter=request.user
            product.save()
            return redirect('home')
        else:
            return render(request,'product/create.html',{'error':"Fill all the fields"})
    else:
        return render(request,'product/create.html')
    
