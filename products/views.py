from django.shortcuts import render

# Create your views here.

def all_products(request):
    """ A view to who all products with sorting and search queries """

    products =  Product.objects.all()

    context = [
        'products': products,
    ]

    return render(request, 'products/products.html', context)
