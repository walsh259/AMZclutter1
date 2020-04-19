from django.http import HttpResponse, Http404
from django.shortcuts import render
from .forms import ContactForm
from .models import Product
from .models import Supplier
from .models import Designer
# from .models import Suppliers
#

def contact(request):

    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():

            name = form.cleaned_data['name']
            email = form.cleaned_data['email']

            print(name, email)

    form = ContactForm()
    return render(request, 'clutter/contact.html', {'form': form})

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
        "designers": Designer.objects.all()
    }
    return render(request, 'clutter/designers.html', context)

def designer(request, designer_id):
    try:
        designer = Designer.objects.get(pk=designer_id)
    except designer.DoesNotExist:
        raise Http404("Designer does not exist.")
    context = {
    "designer": designer
    }
    return render(request, "clutter/designer.html", context)

def files(request):
    context = {
        "products": Product.objects.all()
    }
    return render(request, 'clutter/files.html', context)

def uploads(request):
    context = {
        "products": Product.objects.all()
    }
    return render(request, 'clutter/uploads.html', context)

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
