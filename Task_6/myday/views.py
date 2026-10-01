from django.shortcuts import render
from django.http import HttpResponseRedirect
from myday.models import Product
from django.urls import reverse

def newProductForm(request):
    res = render(request, 'newProductForm.html')
    return res


def createProduct(request):
    p_id = request.POST[p_id]
    p_name = request.POST[p_name]
    p_price = request.POST[p_price]
    p_offer = request.POST[p_offer]
    pro = Product(p_id=p_id, p_name=p_name, p_price=p_price, p_offer=p_offer)
    pro.save()
    url=reverse('productlist')
    return HttpResponseRedirect(url)

def productlist(request):         # read Records (R of CRUD)
    Product = Product.objects.all()
    res = render(request, 'productlist.html', {'Product':Product})
    return res


# Create your views here.
