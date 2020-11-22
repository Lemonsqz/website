"""mysite URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.conf import settings
from django.contrib import admin
from django.urls import path, include
from base.views import *
from django.conf.urls.static import static


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', IndexView.as_view(), name='home'),
    path('accessories', AccessoryList.as_view(), name='acces'),
    path('smartphones', PhoneList.as_view(), name='phones'),
    path('notebooks', NotebookList.as_view(), name='notebooks'),
    path('cart', CartView.as_view(), name='cart'),
    path('phone_detail/<slug>/', PhoneDetailView.as_view(), name='phone_detail'),
    path('access_detail/<slug>/', AccessoryDetailView.as_view(), name='access_detail'),
    path('notebook_detail/<slug>/', NotebookDetailView.as_view(), name='notebook_detail'),
    path('add-to-cart/<slug>/',AddToCartView.as_view(), name='add_to_cart'),
    path('summernote/', include('django_summernote.urls')),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)