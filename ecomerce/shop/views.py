from django.shortcuts import render
from django.http import HttpResponse
from .models import product
from math import ceil
def index(request):
    # products=product.objects.all() 
    # params={'no_of_slides':nslides, 'range':range(1,nslides), 'product':products}
    # allProds=[[products, range(1, nSlides), nSlides],[products, range(1, nSlides), nSlides]]
    allprods=[]
    catprod=product.objects.values('category','id')
    cats={item['category'] for item in catprod}
    for cat in cats:
        prod=product.objects.filter(category=cat)
        n=len(prod)
        nSlides=n//4 + ceil((n/4)-(n//4))
        allprods.append([prod,range(1,nSlides),nSlides])

    params={'allProds':allprods }
    return render(request,'shop/index.html',params)

def about(request):
    return render(request,'shop/about.html')
def contact(request):
    return HttpResponse("we are at contact")

def tracker(request):
    return HttpResponse("we are at tracker")

def search(request):
    return HttpResponse("we are at search")

def productviews(request):
    return HttpResponse("we are at productviews")

def checkout(request):
    return HttpResponse("we are at checkout")
