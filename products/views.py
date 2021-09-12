from django.shortcuts import render, get_object_or_404

# Create your views here.

def all_products(request):
    """ A view for product details """

    products =  Product.objects.all(Product, pk=product_id )

    context = [
        'product': products,
    ]

    return render(request, 'products/products.html', context)
