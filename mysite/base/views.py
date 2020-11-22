from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.shortcuts import render, redirect
from django.http import HttpResponseRedirect
# Create your views here.
from django.views import View
from django.views.generic import DetailView, ListView

from base.models import Phone, Accessory, Notebook, Customer, Cart


class IndexView(View):

    def get(self, request, *args, **kwargs):
        phones = Phone.objects.all().order_by('-date')[:3]
        notebooks = Notebook.objects.all().order_by('-date')[:3]
        context = {
            'phone_list': phones,
            'notebook_list': notebooks,

        }
        return render(request, 'index.html', context)


class AddToCartView(View):

    def get(self, request, *args, **kwargs):
        return HttpResponseRedirect('cart')


class CartView(View):

    def get(self, request, *args, **kwargs):
        customer = Customer.objects.get(user=request.user)
        cart = Cart.objects.get(owner=customer)
        context = {
            'cart': cart
        }
        return render(request, 'cart.html', context)


class PhoneDetailView(DetailView):
    model = Phone
    context_object_name = 'phones'
    template_name = 'phone_detail.html'
    slug_url_kwarg = 'slug'


class AccessoryList(ListView):
    model = Accessory
    context_object_name = 'access'
    paginate_by = 2
    template_name = 'empty_section.html'


class AccessoryDetailView(DetailView):
    model = Accessory
    context_object_name = 'access'
    template_name = 'access_detail.html'


class PhoneList(ListView):
    model = Phone
    queryset = Phone.objects.all()
    context_object_name = 'phones'
    paginate_by = 2
    template_name = 'smartphones.html'


class NotebookList(ListView):
    model = Notebook
    queryset = Notebook.objects.all()
    context_object_name = 'notebooks'
    paginate_by = 2
    template_name = 'notebooks.html'


class NotebookDetailView(DetailView):
    model = Notebook
    context_object_name = 'notebooks'
    template_name = 'notebook_detail.html'
    slug_url_kwarg = 'slug'
