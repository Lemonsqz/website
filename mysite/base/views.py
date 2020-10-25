from django.shortcuts import render

# Create your views here.
from django.views.generic import DetailView, ListView

from base.models import Product


class IndexListView(ListView):
    model = Product
    template_name = 'index.html'


def cart(request):
    return render(request, 'cart.html')


class ProductDetailView(DetailView):
    model = Product
    template_name = 'phone.html'
