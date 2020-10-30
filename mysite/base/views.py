from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.shortcuts import render, redirect

# Create your views here.
from django.views.generic import DetailView, ListView

from base.models import Product


class IndexListView(ListView):
    queryset = Product.objects.all().order_by('-date')[:3]
    model = Product
    template_name = 'index.html'


def cart(request):
    return render(request, 'cart.html')


class ProductDetailView(DetailView):
    context_object_name = 'product'
    model = Product
    template_name = 'phone.html'


class AccessoryListView(ListView):
    model = Product
    template_name = 'empty_section.html'


def smartphone(request):
    phones_list = Product.objects.all()
    paginator = Paginator(phones_list, 2)
    page = request.GET.get('page', 1)

    try:
        phones = paginator.page(page)

    except PageNotAnInteger:
        phones = paginator.page(1)

    except EmptyPage:
        phones = paginator.page(paginator.num_pages)

    return render(request, 'smartphones.html', {'page': page, 'phones': phones, 'objects': phones_list})
