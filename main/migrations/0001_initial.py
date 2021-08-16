# Generated by Django 3.2.1 on 2021-06-25 16:01

from django.db import migrations, models
import django.db.models.deletion
import main.models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=100, unique=True)),
            ],
        ),
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100, verbose_name='Sarlavha')),
                ('price', models.DecimalField(decimal_places=2, max_digits=9, verbose_name='Narxi')),
                ('image', models.ImageField(upload_to=main.models.convert_image, verbose_name='Rasm')),
                ('repair_service', models.CharField(blank=True, max_length=200, verbose_name='Servis xizmat')),
                ('warranty', models.CharField(blank=True, max_length=200, verbose_name='Kafolat mudati')),
                ('category', models.ForeignKey(blank=True, on_delete=django.db.models.deletion.CASCADE, to='main.category', verbose_name='Kategoriya tanlash')),
            ],
        ),
        migrations.CreateModel(
            name='Gaz',
            fields=[
                ('product_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='main.product')),
                ('size', models.CharField(blank=True, max_length=200, verbose_name='Hajmi')),
                ('cage', models.CharField(blank=True, max_length=200, verbose_name='Panjara turi')),
                ('energy_type', models.CharField(blank=True, max_length=200, verbose_name='Energiya turi')),
                ('sales', models.BooleanField(blank=True, choices=[(True, 'BOR'), (False, 'YOQ')], null=True, verbose_name='Sotuvda')),
                ('color', models.CharField(blank=True, max_length=100, verbose_name='Rangi')),
                ('additional_data', models.TextField(blank=True, verbose_name="Qo'shimacha malumotlari")),
            ],
            bases=('main.product',),
        ),
        migrations.CreateModel(
            name='Konditsaner',
            fields=[
                ('product_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='main.product')),
                ('energy', models.CharField(blank=True, max_length=200, verbose_name='Energiya samaradorligi')),
                ('invertor', models.CharField(blank=True, max_length=100, verbose_name='Kompressorning invertor turi')),
                ('sales', models.BooleanField(blank=True, choices=[(True, 'BOR'), (False, 'YOQ')], null=True, verbose_name='Sotuvda')),
                ('additional_data', models.TextField(blank=True, verbose_name="Qo'shimacha malumotlari")),
            ],
            bases=('main.product',),
        ),
        migrations.CreateModel(
            name='Muzlatkich',
            fields=[
                ('product_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='main.product')),
                ('size', models.CharField(max_length=200, verbose_name='Hajmi')),
                ('color', models.CharField(blank=True, max_length=100, verbose_name='Rangi')),
                ('energy', models.CharField(max_length=200, verbose_name='Energiya samaradorligi')),
                ('freezers', models.CharField(max_length=200, verbose_name='Kameralar soni')),
                ('invertor', models.CharField(max_length=100, verbose_name='Kompressorning invertor turi')),
                ('sales', models.BooleanField(blank=True, choices=[(True, 'BOR'), (False, 'YOQ')], null=True, verbose_name='Sotuvda')),
            ],
            bases=('main.product',),
        ),
        migrations.CreateModel(
            name='Notebook',
            fields=[
                ('product_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='main.product')),
                ('diagonal', models.CharField(max_length=100, verbose_name='Ekran hajmi')),
                ('display_type', models.CharField(max_length=100, verbose_name='Ekran turi')),
                ('prosessor', models.CharField(max_length=100, verbose_name='Protsessor turi')),
                ('ram', models.CharField(max_length=100, verbose_name='Operativ xotira')),
                ('video', models.CharField(max_length=100, verbose_name='Video karta')),
                ('color', models.CharField(blank=True, max_length=100, verbose_name='Rangi')),
                ('battery', models.CharField(max_length=100, verbose_name='Batareya quvvati')),
                ('sales', models.BooleanField(blank=True, choices=[(True, 'BOR'), (False, 'YOQ')], null=True, verbose_name='Sotuvda')),
            ],
            bases=('main.product',),
        ),
        migrations.CreateModel(
            name='Smartphone',
            fields=[
                ('product_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='main.product')),
                ('diagonal', models.CharField(max_length=100, verbose_name='Ekran hajmi')),
                ('display_type', models.CharField(max_length=100, verbose_name='Ekran turi')),
                ('ram', models.CharField(max_length=100, verbose_name='Operativ xotira')),
                ('sd', models.CharField(max_length=100, verbose_name='Asosiy xotira')),
                ('camera', models.CharField(max_length=100, verbose_name='Asosiy kamera')),
                ('front_camera', models.CharField(max_length=100, verbose_name='Old kamera')),
                ('color', models.CharField(blank=True, max_length=100, verbose_name='Rangi')),
                ('battery', models.CharField(max_length=100, verbose_name='Batareya quvvati')),
                ('sales', models.BooleanField(blank=True, choices=[(True, 'BOR'), (False, 'YOQ')], null=True, verbose_name='Sotuvda')),
            ],
            bases=('main.product',),
        ),
        migrations.CreateModel(
            name='Televizor',
            fields=[
                ('product_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='main.product')),
                ('diagonal', models.CharField(max_length=100, verbose_name='Ekran hajmi')),
                ('display_type', models.CharField(max_length=100, verbose_name='Ekran turi')),
                ('color', models.CharField(blank=True, max_length=100, verbose_name='Rangi')),
                ('sales', models.BooleanField(blank=True, choices=[(True, 'BOR'), (False, 'YOQ')], null=True, verbose_name='Sotuvda')),
                ('additional_data', models.TextField(blank=True, verbose_name="Qo'shimacha malumotlari")),
            ],
            bases=('main.product',),
        ),
    ]
