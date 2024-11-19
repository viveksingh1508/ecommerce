from django.urls import path
from base.views import product


urlpatterns = [
    path("", product.getProducts, name="products"),
    path("<str:pk>/", product.getProduct, name="product"),
]
