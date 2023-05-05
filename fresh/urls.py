from django.urls import path
from . import views
from django.contrib.staticfiles.urls import staticfiles_urlpatterns


app_name = 'fresh'
urlpatterns = [
    path('', views.index),
    path('shop', views.shop, name='shop'),
    path('category/<int:id>/', views.category, name="category"),
    path('descriptions/<int:id>/', views.descriptions, name="description"),
]
urlpatterns += staticfiles_urlpatterns()


