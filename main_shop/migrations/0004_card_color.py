# Generated by Django 3.2.1 on 2021-06-28 17:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main_shop', '0003_auto_20210628_1754'),
    ]

    operations = [
        migrations.AddField(
            model_name='card',
            name='color',
            field=models.CharField(default=1, max_length=50, verbose_name='Maxsulot rangi'),
            preserve_default=False,
        ),
    ]
