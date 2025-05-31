from django.shortcuts import render, get_object_or_404
from cart.forms import CartAddProductForm
from .models import Category, Product
from django.core.mail import send_mail
from django.conf import settings


def product_list(request, category_slug=None):
    category = None
    categories = Category.objects.all()
    products = Product.objects.filter(available=True)
    
    if category_slug:
        category = get_object_or_404(Category, slug=category_slug)
        products = products.filter(category=category)
    
    # Добавляем русскоязычные заголовки в контекст
    context = {
        'category': category,
        'categories': categories,
        'products': products,
        'page_title': 'Каталог товаров',
        'category_title': 'Все категории' if not category else f'Категория: {category.name}',
        'products_title': 'Доступные товары',
    }
    
    return render(request, 'shop/product/list.html', context)


def product_detail(request, id, slug):
    product = get_object_or_404(Product, id=id, slug=slug, available=True)
    cart_product_form = CartAddProductForm()
    
    # Добавляем русскоязычные заголовки в контекст
    context = {
        'product': product,
        'cart_product_form': cart_product_form,
        'page_title': f'Товар: {product.name}',
        'details_title': 'Описание товара',
        'price_title': 'Цена',
        'add_to_cart_title': 'Добавить в корзину',
    }
    
    return render(request, 'shop/product/detail.html', context)


def about(request):
    return render(request, 'shop/about.html')



def contacts(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        phone = request.POST.get('phone')
        message = request.POST.get('message')
        
        # Отправка email
        send_mail(
            f'Сообщение от {name}',
            f'Имя: {name}\nEmail: {email}\nТелефон: {phone}\n\nСообщение:\n{message}',
            settings.DEFAULT_FROM_EMAIL,
            [settings.CONTACT_EMAIL],
            fail_silently=False,
        )
        
        return render(request, 'shop/contacts.html', {'success': True})
    
    return render(request, 'shop/contacts.html')