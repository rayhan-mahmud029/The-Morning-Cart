from unicodedata import category
from django.shortcuts import render
from django.http import HttpResponse
from .models import Product
from .models import HomeBanner
from .models import Sale
from .models import Featured
def index(request):
    items = Product.objects.all()
    banners = HomeBanner.objects.all()
    sales = Sale.objects.all()
    featureProds = []
    catfProds = Featured.objects.values('category', 'id')
    fCats = {item['category'] for item in catfProds}
    for cat in fCats:
        fProd = Featured.objects.filter(category=cat)
        featureProds.append(fProd)
    return render(request, 'shop/index.html',{'products': items, 'banners': banners, 'sales': sales, 'featureds': featureProds})

def checkout(request):
    return HttpResponse("This is checkout View page...")

def about(request):
    return HttpResponse("This is about page...")

def contactUs(request):
    return HttpResponse("This is contactUs View page...")

def search(request):
    return HttpResponse("This is search page...")

def product(request):
    allProducts = []
    catProds = Product.objects.values('category','id')
    categories = {item['category'] for item in catProds}
    for cat in categories:
        products = Product.objects.filter(category=cat)
        allProducts.append(products)


    return render(request, 'shop/products.html',{'products': allProducts})


# Create your views here.
