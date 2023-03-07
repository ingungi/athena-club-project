from django.urls import path, include

from product import views

urlpatterns = [
    path('carousel-products/', views.CarouselProductsList.as_view()),
    path('products/', views.getProduct.as_view()),
]