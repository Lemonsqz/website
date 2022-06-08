from django.shortcuts import reverse
from django.db import models
from django.utils.timezone import now
from django.contrib.auth import get_user_model

User = get_user_model()


# def get_product_url(obj, viewname):
# testgit
#     ct_model = obj.__class__._meta.model_name
#     return reverse(viewname, kwargs={'ct_model': ct_model, 'slug': obj.slug})


# Create your models here.

class Category(models.Model):
    title = models.CharField(max_length=255, verbose_name="Название категории")

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Категория'
        verbose_name_plural = 'Категории'


class Phone(models.Model):
    category = models.ForeignKey(Category, verbose_name="Категория", on_delete=models.CASCADE, blank=True, null=True)
    name = models.CharField(max_length=50, blank=True, verbose_name="Название")
    description = models.TextField(blank=True, null=True, verbose_name="Описание")
    price = models.DecimalField(decimal_places=2, max_digits=10000, null=True, blank=True, verbose_name="Цена")
    date = models.DateTimeField(default=now, blank=True, null=True, verbose_name="Дата")
    img = models.TextField(max_length=500, blank=True, verbose_name="Изображение")
    add_img = models.TextField(max_length=500, blank=True, verbose_name="Дополнительно")
    slug = models.SlugField()

    class Meta:
        verbose_name = 'Телефон'
        verbose_name_plural = 'Телефоны'

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse("phone_detail", kwargs={
            'slug': self.slug
        })


class Accessory(models.Model):
    category = models.ForeignKey(Category, verbose_name="Категория", on_delete=models.CASCADE, blank=True, null=True)
    name = models.CharField(max_length=50, blank=True, verbose_name="Название")
    description = models.TextField(blank=True, null=True, verbose_name="Описание")
    price = models.DecimalField(decimal_places=2, max_digits=10000, null=True, blank=True, verbose_name="Цена")
    date = models.DateTimeField(default=now, blank=True, null=True, verbose_name="Дата")
    img = models.TextField(max_length=500, blank=True, verbose_name="Изображение")
    add_img = models.TextField(max_length=500, blank=True, verbose_name="Дополнительно")
    slug = models.SlugField()

    class Meta:
        verbose_name = 'Аксессуар'
        verbose_name_plural = 'Аксессуары'

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse("access_detail", kwargs={
            'slug': self.slug
        })


class Notebook(models.Model):
    category = models.ForeignKey(Category, verbose_name="Категория", on_delete=models.CASCADE, blank=True, null=True)
    name = models.CharField(max_length=50, blank=True, verbose_name="Название")
    description = models.TextField(blank=True, null=True, verbose_name="Описание")
    price = models.DecimalField(decimal_places=2, max_digits=10000, null=True, blank=True, verbose_name="Цена")
    date = models.DateTimeField(default=now, blank=True, null=True, verbose_name="Дата")
    img = models.TextField(max_length=500, blank=True, verbose_name="Изображение")
    add_img = models.TextField(max_length=500, blank=True, verbose_name="Дополнительно")
    slug = models.SlugField()

    class Meta:
        verbose_name = 'Ноутбук'
        verbose_name_plural = 'Ноутбуки'

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse("notebook_detail", kwargs={
            'slug': self.slug
        })


class CartProduct(models.Model):
    user = models.ForeignKey('Customer', verbose_name='Покупатель', on_delete=models.CASCADE)
    cart = models.ForeignKey('Cart', verbose_name='Корзина', on_delete=models.CASCADE, related_name='related_products')
    product = models.ForeignKey(Phone, verbose_name='Товар', on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(default=1)
    final_price = models.DecimalField(max_digits=9, decimal_places=2, verbose_name='Общая цена')

    def __str__(self):
        return 'Продукт: {} (для корзины)'.format(self.product.name)


class Cart(models.Model):
    owner = models.ForeignKey('Customer', verbose_name='Владелец', on_delete=models.CASCADE)
    products = models.ManyToManyField(CartProduct, blank=True, related_name='related_cart')
    total_products = models.PositiveIntegerField(default=0)
    final_price = models.DecimalField(max_digits=9, decimal_places=2, verbose_name='Общая цена')
    in_order = models.BooleanField(default=False)
    for_anonymous_user = models.BooleanField(default=False)

    def __str__(self):
        return str(self.id)

    class Meta:
        verbose_name = 'Корзина'
        verbose_name_plural = 'Корзина'


class Customer(models.Model):
    user = models.ForeignKey(User, verbose_name='Пользователь', on_delete=models.CASCADE)
    phone = models.CharField(max_length=25, verbose_name='Номер телефона')
    address = models.CharField(max_length=255, verbose_name='Адрес')

    def __str__(self):
        return 'Покупатель: {} {}'.format(self.user.first_name, self.user.last_name)

    class Meta:
        verbose_name = 'Покупатель'
        verbose_name_plural = 'Покупатели'
