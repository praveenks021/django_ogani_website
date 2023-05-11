from django.shortcuts import render, HttpResponse, redirect
from .models import *
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.shortcuts import get_object_or_404
from django.db.models import Q



def index(request):
    category_list = Category.objects.all()
    return render(request, 'index.html', {"category_list": category_list})


def shop(request):
    items = Product.objects.all()
    return render(request, 'shop.html', {"items": items})


def category(request, id):
    products = Product.objects.filter(category__id=id)
    return render(request, "shop-grid.html", {"products": products})


def descriptions(request, id):
    product_description = Product.objects.filter(id=id)
    return render(request, "shop-details.html", {"product_description": product_description})


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
            return HttpResponse("Your password and confrom password are not Same!!")
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
    total = 0
    grand_total = 0
    cart_items = Cart.objects.filter(user=request.user)
    for i in cart_items:
        total = i.quantity * i.products.price
        grand_total = grand_total+total
    context = {'cart_items': cart_items, 'total': total, 'grand_total': grand_total}
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
    context = {'wishlist_items': wishlist_items}
    return render(request, "wishlist.html", context)


def del_wishlist_item(request, id):
    product = Wishlist.objects.get(id=id)
    product.delete()
    return redirect("/wishlist")




