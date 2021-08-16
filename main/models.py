from django.db import models
from datetime import datetime
import os
from PIL import Image
from io import BytesIO
from django.core.files import File
from django.contrib.auth.models import User

BOOL_CHOICES = [
    (True, 'BOR'),
    (False, "YOQ")
]


def convert_image(ins, file):
    ext = file.split('.')[-1]
    filname = '{:%Y-%m-%d-%H-%M-%S}.{}'.format(datetime.now(), ext)
    return os.path.join('product_image', filname)

class Category(models.Model):
    name = models.CharField(max_length=100, unique=True, blank=True)
    def __str__(self):
        return self.name

class Product(models.Model):
    category = models.ForeignKey(Category, verbose_name="Kategoriya tanlash", on_delete=models.CASCADE, blank=True)
    title = models.CharField(max_length=100, verbose_name="Sarlavha")
    price = models.DecimalField(max_digits=9, decimal_places=2, verbose_name="Narxi")
    image = models.ImageField(upload_to=convert_image, verbose_name="Rasm")
    repair_service = models.CharField(max_length=200, verbose_name="Servis xizmat", blank=True)
    warranty = models.CharField(max_length=200, verbose_name="Kafolat mudati", blank=True)

    def save(self, *args, **kwargs):
        if not self.image.closed:
            img = Image.open(self.image)
            img.thumbnail((600, 600), Image.ANTIALIAS)
            tmp = BytesIO()
            img.save(tmp, 'PNG')
            self.image = File(tmp, 't.png')
        return super().save(*args, **kwargs)


class Notebook(Product):
    diagonal = models.CharField(max_length=100, verbose_name="Ekran hajmi")
    display_type = models.CharField(max_length=100, verbose_name="Ekran turi")
    prosessor = models.CharField(max_length=100, verbose_name="Protsessor turi")
    ram = models.CharField(max_length=100, verbose_name="Operativ xotira")
    video = models.CharField(max_length=100, verbose_name="Video karta")
    color = models.CharField(max_length=100, verbose_name="Rangi", blank=True)
    battery = models.CharField(max_length=100, verbose_name="Batareya quvvati")
    sales = models.BooleanField(choices=BOOL_CHOICES, verbose_name="Sotuvda", null=True, blank=True)


class Smartphone(Product):
    diagonal = models.CharField(max_length=100, verbose_name="Ekran hajmi")
    display_type = models.CharField(max_length=100, verbose_name="Ekran turi")
    ram = models.CharField(max_length=100, verbose_name="Operativ xotira")
    sd = models.CharField(max_length=100, verbose_name="Asosiy xotira")
    camera = models.CharField(max_length=100, verbose_name="Asosiy kamera")
    front_camera = models.CharField(max_length=100, verbose_name="Old kamera")
    color = models.CharField(max_length=100, verbose_name="Rangi", blank=True)
    battery = models.CharField(max_length=100, verbose_name="Batareya quvvati")
    sales = models.BooleanField(choices=BOOL_CHOICES, verbose_name="Sotuvda", null=True, blank=True)


class Televizor(Product):
    diagonal = models.CharField(max_length=100, verbose_name="Ekran hajmi")
    display_type = models.CharField(max_length=100, verbose_name="Ekran turi")
    color = models.CharField(max_length=100, verbose_name="Rangi", blank=True)
    sales = models.BooleanField(choices=BOOL_CHOICES, verbose_name="Sotuvda", null=True, blank=True)
    additional_data = models.TextField(verbose_name="Qo'shimacha malumotlari", blank=True)



class Muzlatkich(Product):
    size = models.CharField(max_length=200, verbose_name="Hajmi")
    color = models.CharField(max_length=100, verbose_name="Rangi", blank=True)
    energy = models.CharField(max_length=200, verbose_name="Energiya samaradorligi")
    freezers = models.CharField(max_length=200, verbose_name="Kameralar soni")
    invertor = models.CharField(max_length=100, verbose_name="Kompressorning invertor turi")
    sales = models.BooleanField(choices=BOOL_CHOICES, verbose_name="Sotuvda", null=True, blank=True)


class Konditsaner(Product):
    energy = models.CharField(max_length=200, verbose_name="Energiya samaradorligi", blank=True)
    invertor = models.CharField(max_length=100, verbose_name="Kompressorning invertor turi", blank=True)
    sales = models.BooleanField(choices=BOOL_CHOICES, verbose_name="Sotuvda", null=True, blank=True)
    additional_data = models.TextField(verbose_name="Qo'shimacha malumotlari", blank=True)


class Gaz(Product):
    size = models.CharField(max_length=200, verbose_name="Hajmi", blank=True)
    cage = models.CharField(max_length=200, verbose_name="Panjara turi", blank=True)
    energy_type = models.CharField(max_length=200, verbose_name="Energiya turi", blank=True)
    sales = models.BooleanField(choices=BOOL_CHOICES, verbose_name="Sotuvda", null=True, blank=True)
    color = models.CharField(max_length=100, verbose_name="Rangi", blank=True)
    additional_data = models.TextField(verbose_name="Qo'shimacha malumotlari", blank=True)