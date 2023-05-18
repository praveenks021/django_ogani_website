from django.urls import path
from . import views
from django.contrib.staticfiles.urls import staticfiles_urlpatterns


app_name = 'fresh'
urlpatterns = [
    path('', views.index),
    path('shop', views.shop, name='shop'),
    path('category/<int:id>/', views.category, name="category"),
    path('descriptions/<int:id>/', views.descriptions, name="description"),
    path("blog", views.blog, name="blog"),
    path("contact", views.contact, name="contact"),
    path('login/', views.LoginPage, name='login'),
    path('logout/', views.LogoutPage, name='logout'),
    path('signup/', views.SignupPage, name='signup'),
    path("cart_objects/<str:pname>", views.cart_objects, name="cart_objects"),
    path('cart_items', views.viewcart, name='cart_items'),
    path('del_cart_item/<int:id>', views.del_cart_item, name='del_cart_item'),
    path("wishlist_objects/<str:pname>", views.wishlist_objects, name="wishlist_objects"),
    path('wishlist', views.wishlist, name='wishlist'),
    path('del_wishlist_item/<int:id>', views.del_wishlist_item, name='del_wishlist_item'),
    path('search_product', views.search_product, name='search_product'),
    path("checkout", views.checkout, name="checkout"),
    path("increment/<int:id>/", views.increment, name="increment"),
    path("decrement/<int:id>/", views.decrement, name="decrement"),
    path('sort_name', views.sort_name, name='sort_name'),
    path('sort_price', views.sort_price, name='sort_price'),

]
urlpatterns += staticfiles_urlpatterns()


