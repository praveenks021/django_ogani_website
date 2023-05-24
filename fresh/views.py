from django.shortcuts import render, HttpResponse, redirect
from .models import *
from .forms import CheckoutForm
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.shortcuts import get_object_or_404
from django.db.models import Max, Min


def index(request):
    category_list = Category.objects.all()
    wishlist_quantity = Wishlist.objects.all().count()
    cart_quantity = Cart.objects.all().count()
    featured = Featured.objects.all()
    return render(request, 'index.html', {"category_list": category_list,
                                          'wishlist_quantity': wishlist_quantity,
                                          'cart_quantity': cart_quantity,
                                          'featured': featured})


def shop(request):
    min_price = Product.objects.all().aggregate(Min('price'))
    max_price = Product.objects.all().aggregate(Max('price'))
    FilterPrice = request.GET.get('FilterPrice')
    if FilterPrice:
        Int_FilterPrice = int(FilterPrice)
        items = Product.objects.filter(price__lte=Int_FilterPrice)
    else:
        items = Product.objects.all()
    category_list = Category.objects.all()
    latest_product = Product.objects.order_by('-id')[0:4]
    wishlist_quantity = Wishlist.objects.all().count()
    cart_quantity = Cart.objects.all().count()
    return render(request, 'shop.html', {"items": items, 'category_list': category_list,
                                         'min_price': min_price, 'max_price': max_price,
                                         'latest_product': latest_product,
                                         'wishlist_quantity': wishlist_quantity,
                                         'cart_quantity': cart_quantity})


def category(request, id):
    category_list = Category.objects.all()
    products = Product.objects.filter(category__id=id)
    latest_product = Product.objects.order_by('-id')[0:4]
    wishlist_quantity = Wishlist.objects.all().count()
    cart_quantity = Cart.objects.all().count()
    return render(request, "shop-grid.html", {"products": products, 'category_list': category_list,
                                              'latest_product': latest_product,
                                              'wishlist_quantity': wishlist_quantity,
                                              'cart_quantity': cart_quantity
                                              })


def descriptions(request, id):
    is_in_cart = False
    product_description = Product.objects.get(id=id)
    cart = Cart.objects.filter(products=product_description)
    if len(cart) > 0:
        is_in_cart = True
    wishlist_quantity = Wishlist.objects.all().count()
    cart_quantity = Cart.objects.all().count()
    return render(request, "shop-details.html", {"product_description": product_description,
                                                 'wishlist_quantity': wishlist_quantity,
                                                 'cart_quantity': cart_quantity, 'is_in_cart': is_in_cart})


def blog(request):
    return render(request, "blog.html")


def contact(request):
    return render(request, "contact.html")


def SignupPage(request):
    if request.method == 'POST':
        uname = request.POST.get('username')
        email = request.POST.get('email')
        pass1 = request.POST.get('password1')
        pass2 = request.POST.get('password2')
        if pass1 != pass2:
            return HttpResponse("Your password and conform password are not Same!!")
        else:

            my_user = User.objects.create_user(uname, email, pass1)
            my_user.save()
            return redirect('/login')

    return render(request, 'signup.html')


def LoginPage(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        pass1 = request.POST.get('pass')
        user = authenticate(request, username=username, password=pass1)
        if user is not None:
            login(request, user)
            return redirect('/')
        else:
            return HttpResponse("Username or Password is incorrect!!!")

    return render(request, 'login.html')


def LogoutPage(request):
    logout(request)
    return redirect('/')


def cart_objects(request, pname):
    cart_items = get_object_or_404(Product, pname=pname)
    username = request.user
    cart = Cart.objects.create(user=username, products=cart_items, quantity=1)
    cart.save()
    return redirect("/cart_items")


def viewcart(request):
    grand_total = 0
    cart_items = Cart.objects.filter(user=request.user)
    wishlist_quantity = Wishlist.objects.all().count()
    cart_quantity = Cart.objects.all().count()
    for i in cart_items:
        grand_total = grand_total+i.get_total()
    if grand_total < 99:
        grand_total = grand_total+5
    context = {'cart_items': cart_items, 'grand_total': grand_total, 'wishlist_quantity': wishlist_quantity,
               'cart_quantity': cart_quantity}
    return render(request, "shoping-cart.html", context)


def del_cart_item(request, id):
    product = Cart.objects.get(id=id)
    product.delete()
    return redirect("/cart_items")


def wishlist_objects(request, pname):
    wishlist_items = get_object_or_404(Product, pname=pname)
    username = request.user
    wishlist = Wishlist.objects.create(user=username, products=wishlist_items)
    wishlist.save()
    return redirect("/wishlist")


def wishlist(request):
    wishlist_items = Wishlist.objects.filter(user=request.user)
    category_list = Category.objects.all()
    wishlist_quantity = Wishlist.objects.all().count()
    cart_quantity = Cart.objects.all().count()
    context = {'wishlist_items': wishlist_items, 'category_list': category_list,
               'wishlist_quantity': wishlist_quantity, 'cart_quantity': cart_quantity}
    return render(request, "wishlist.html", context)


def del_wishlist_item(request, id):
    product = Wishlist.objects.get(id=id)
    product.delete()
    return redirect("/wishlist")


def search_product(request):
    category_list = Category.objects.all()
    wishlist_quantity = Wishlist.objects.all().count()
    cart_quantity = Cart.objects.all().count()
    if request.method == "POST":
        query_name = request.POST.get('pname')
        if query_name:
            results = Product.objects.filter(pname__contains=query_name)
            return render(request, 'searchlist.html', {"results": results, 'category_list': category_list,
                                                       'wishlist_quantity': wishlist_quantity,
                                                       'cart_quantity': cart_quantity})
    return render(request, 'searchlist.html')


def increment(request, id):
    if request.method == "GET":
        item = Cart.objects.get(pk=id)
        if 0 < (item.quantity + 1):
            item.quantity += 1
            item.save()
            return redirect('/cart_items')
    return redirect('/cart_items')


def decrement(request, id):
    if request.method == "GET":
        item = Cart.objects.get(pk=id)
        if 0 < (item.quantity - 1):
            item.quantity -= 1
            item.save()
            return redirect('/cart_items')
    return redirect('/cart_items')


def checkout(request):
    total = 0
    grand_total = 0
    cart_items = Cart.objects.filter(user=request.user)
    for i in cart_items:
        total = i.quantity * i.products.price
        grand_total = grand_total + total
    if grand_total < 99:
        grand_total = grand_total+5
    if request.method == "POST":
        form = CheckoutForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("/")
    else:
        form = CheckoutForm()
    return render(request, 'checkout.html', {'cart_items': cart_items, 'grand_total': grand_total})


def sort_name(request):
    items = Product.objects.all().order_by('pname')
    category_list = Category.objects.all()
    return render(request, 'shop.html', {"items": items, 'category_list': category_list})


def sort_price(request):
    items = Product.objects.all().order_by('price')
    category_list = Category.objects.all()
    return render(request, 'shop.html', {"items": items, 'category_list': category_list})
