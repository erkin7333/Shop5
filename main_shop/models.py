from django.db import models
from datetime import datetime
import os
from PIL import Image
from io import BytesIO
from django.core.files import File
from django.contrib.auth import get_user_model
User = get_user_model()

class Category(models.Model):
    name = models.CharField(max_length=150, verbose_name="Categoriyalar nomi")
    def __str__(self):
        return self.name

class Brand(models.Model):
    brand_name = models.CharField(max_length=150, verbose_name="Brend nomi")
    def __str__(self):
        return self.brand_name

BOOL_CHOICES = [
    (True, "BOR"),
    (False, "YOQ")
]

def brand_image(ins, file):
    ext = file.split('.')[-1]
    filname = '{:%Y-%m-%d-%H-%M-%S}.{}'.format(datetime.now(), ext)
    return os.path.join('brand_image', filname)

class Product(models.Model):
    subject = models.CharField(max_length=150, verbose_name="Mavzu")
    content = models.CharField(max_length=150, verbose_name="Malumoti")
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    brand = models.ForeignKey(Brand, on_delete=models.CASCADE)
    sales = models.BooleanField(choices=BOOL_CHOICES, verbose_name="Sotuvda", null=True, blank=True)
    repair_service = models.CharField(max_length=200, verbose_name="Servis xizmat", blank=True)
    warranty = models.CharField(max_length=200, verbose_name="Kafolat mudati", blank=True)
    color = models.CharField(max_length=50, verbose_name="Maxsulot rangi")
    price = models.FloatField( verbose_name="Narxi")
    additional_data = models.TextField(verbose_name="Qo'shimacha malumotlari")
    images = models.ImageField(upload_to=brand_image, verbose_name="Rasm")

    def save(self, *args, **kwargs):
        if not self.images.closed:
            img = Image.open(self.images)
            img.thumbnail((600, 600), Image.ANTIALIAS)
            tmp = BytesIO()
            img.save(tmp, 'PNG')
            self.images = File(tmp, 't.png')
        return super().save(*args, **kwargs)

class Card(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, blank=True)
    card_category = models.CharField(max_length=150, verbose_name="Categorya nomi")
    card_brand = models.CharField(max_length=150, verbose_name="Bend nomi")
    content = models.CharField(max_length=150, verbose_name="Malumoti")
    color = models.CharField(max_length=50, verbose_name="Maxsulot rangi")
    price = models.CharField(max_length=50, verbose_name="Narxi")
    images = models.CharField(max_length=1000, verbose_name="Rasm")


class Adress(models.Model):
    ca = models.ForeignKey(Card, on_delete=models.RESTRICT, blank=True)
    viloyat = models.CharField(max_length=100, verbose_name="Viloyat")
    tuman = models.CharField(max_length=100, verbose_name="Tuman")
    mahalla = models.CharField(max_length=250, verbose_name="Mahalla va qishloq nomi ko'cha nomi ")
    full_name = models.CharField(max_length=100, verbose_name="Ism Familya")
    uy_raqami = models.IntegerField(default=0)
    phone = models.CharField(max_length=20, verbose_name='Telefon raqami')
