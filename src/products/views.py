from django.shortcuts import render

from .models import Product

from .forms import ProductForm

# Create your views here.


def product_create_view(request):
    form = ProductForm(request.POST or None)
    if form.is_valid():
        form.save()

    ctx = {
        "form": form
    }
    return render(request=request, template_name="products/create.html", context=ctx)


def product_detail_view(request):
    obj = Product.objects.get(id=1)
    ctx = {
        "title": obj.title,
        "description": obj.description,
        "price": obj.price
    }
    return render(request=request, template_name="products/detail.html", context=ctx)
