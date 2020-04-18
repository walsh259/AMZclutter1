from django.http import HttpResponse, Http404
from django.shortcuts import render
from .models import Product
from .models import Supplier
# from .models import Suppliers
#


def index(request):
    context = {
        "products": Product.objects.all()
    }
    return render(request, 'clutter/index.html', context)

def items(request):
    context = {
        "products": Product.objects.all()
    }
    return render(request, 'clutter/items.html', context)

def potentials(request):
    context = {
        "products": Product.objects.all()
    }
    return render(request, 'clutter/potentials.html', context)

def history(request):
    context = {
        "products": Product.objects.all()
    }
    return render(request, 'clutter/history.html', context)

def designers(request):
    context = {
        "products": Product.objects.all()
    }
    return render(request, 'clutter/designers.html', context)

def files(request):
    context = {
        "products": Product.objects.all()
    }
    return render(request, 'clutter/files.html', context)


def products(request):
    context = {
        "products": Product.objects.all()
    }
    return render(request, 'clutter/products.html', context)


def product(request, product_id):
    try:
        product = Product.objects.get(pk=product_id)
    except Product.DoesNotExist:
        raise Http404("Product does not exist.")
    context = {
    "product": product
    }
    return render(request, "clutter/product.html", context)

def suppliers(request):
    context = {
        "suppliers": Supplier.objects.all()
    }
    return render(request, 'clutter/suppliers.html', context)

def supplier(request, supplier_id):
    try:
        supplier = Supplier.objects.get(pk=supplier_id)
    except Supplier.DoesNotExist:
        raise Http404("Supplier does not exist.")
    context = {
    "supplier": supplier
    }
    return render(request, "clutter/supplier.html", context)
