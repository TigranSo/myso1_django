# Generated by Django 3.2.16 on 2023-01-05 09:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0005_auto_20230103_1539'),
    ]

    operations = [
        migrations.AddField(
            model_name='order',
            name='domofon',
            field=models.CharField(default=0, max_length=10, verbose_name='Удобный способ оплаты'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='order',
            name='etaj',
            field=models.CharField(blank=True, max_length=10, verbose_name='Этаж'),
        ),
        migrations.AddField(
            model_name='order',
            name='home',
            field=models.CharField(blank=True, max_length=50, verbose_name='Дом'),
        ),
        migrations.AddField(
            model_name='order',
            name='kvartir',
            field=models.CharField(blank=True, max_length=10, verbose_name='Квартира/офис'),
        ),
        migrations.AddField(
            model_name='order',
            name='location',
            field=models.CharField(blank=True, max_length=10, verbose_name='Улица'),
        ),
        migrations.AddField(
            model_name='order',
            name='podezd',
            field=models.CharField(blank=True, max_length=20, verbose_name='Подъезд'),
        ),
    ]