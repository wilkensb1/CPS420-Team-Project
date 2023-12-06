from django.shortcuts import render, get_object_or_404, redirect
from .models import Category, Product
from cart.forms import CartAddProductForm
from .forms import AddStockForm

# Create your views here.

def product_list(request, category_slug=None):
    category = None
    categories = Category.objects.all()
    products = Product.objects.filter(available=True)
    if category_slug:
        category = get_object_or_404(Category, slug=category_slug)
        products = products.filter(category=category)
    return render(request, 'shop/product/list.html', {'category': category, 'categories': categories, 'products': products})

def product_detail(request, id, slug):
    product = get_object_or_404(Product, id=id, slug=slug, available=True)
    cart_product_form = CartAddProductForm()
    add_stock_form = AddStockForm()

    if request.method == 'POST':
        add_stock_form = AddStockForm(request.POST)
        if add_stock_form.is_valid():
            quantity = add_stock_form.cleaned_data['quantity']
            product.stock += quantity
            product.save()
            return redirect('shop:product_list')
    return render(request,'shop/product/detail.html', {'product': product, 'cart_product_form': cart_product_form, 'add_stock_form': add_stock_form})