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
    path("cart_objects/<str:pname>", views.cart_objects, name="cart_objects"),
    path('login/', views.LoginPage, name='login'),
    path('logout/', views.LogoutPage, name='logout'),
    path('signup/', views.SignupPage, name='signup'),
    path('cart_items', views.viewcart, name='cart_items'),
]
urlpatterns += staticfiles_urlpatterns()


