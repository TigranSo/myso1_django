# Generated by Django 3.2.16 on 2023-01-03 08:46

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('shop', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='order',
            options={'ordering': ['pk'], 'verbose_name_plural': 'Заказы'},
        ),
        migrations.AlterModelOptions(
            name='orderitem',
            options={'ordering': ['pk'], 'verbose_name_plural': 'Элемент заказа'},
        ),
        migrations.AlterModelOptions(
            name='payment',
            options={'ordering': ['pk'], 'verbose_name_plural': 'Платеж'},
        ),
        migrations.AlterModelOptions(
            name='product',
            options={'ordering': ['pk'], 'verbose_name_plural': 'Продукты'},
        ),
        migrations.AlterField(
            model_name='order',
            name='amount',
            field=models.DecimalField(blank=True, decimal_places=2, max_digits=20, null=True, verbose_name='Cумма'),
        ),
        migrations.AlterField(
            model_name='order',
            name='comment',
            field=models.TextField(blank=True, null=True, verbose_name='Комментарий'),
        ),
        migrations.AlterField(
            model_name='order',
            name='payment',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, to='shop.payment', verbose_name='Платеж'),
        ),
        migrations.AlterField(
            model_name='order',
            name='status',
            field=models.CharField(choices=[('1 - Корзина', 'Корзина'), ('2 - Ожидает платежа', 'Ожидает платежа'), ('3 - Оплачено', 'Оплачено')], default='1 - Корзина', max_length=32, verbose_name='Cтатус'),
        ),
        migrations.AlterField(
            model_name='order',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='Пользователь'),
        ),
        migrations.AlterField(
            model_name='orderitem',
            name='discount',
            field=models.DecimalField(decimal_places=2, default=0, max_digits=20, verbose_name='Скидка'),
        ),
        migrations.AlterField(
            model_name='orderitem',
            name='order',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='shop.order', verbose_name='Заказ'),
        ),
        migrations.AlterField(
            model_name='orderitem',
            name='price',
            field=models.DecimalField(decimal_places=2, max_digits=20, verbose_name='Цена'),
        ),
        migrations.AlterField(
            model_name='orderitem',
            name='product',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='shop.product', verbose_name='Продукт'),
        ),
        migrations.AlterField(
            model_name='orderitem',
            name='quantity',
            field=models.PositiveIntegerField(default=1, verbose_name='Количество'),
        ),
        migrations.AlterField(
            model_name='payment',
            name='amount',
            field=models.DecimalField(blank=True, decimal_places=2, max_digits=20, null=True, verbose_name='Cумма'),
        ),
        migrations.AlterField(
            model_name='payment',
            name='comment',
            field=models.TextField(blank=True, null=True, verbose_name='Комментарий'),
        ),
        migrations.AlterField(
            model_name='payment',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='Пользователь'),
        ),
        migrations.AlterField(
            model_name='product',
            name='code',
            field=models.CharField(max_length=255, verbose_name='Код продукта'),
        ),
        migrations.AlterField(
            model_name='product',
            name='image_url',
            field=models.URLField(blank=True, null=True, verbose_name='url изображения'),
        ),
        migrations.AlterField(
            model_name='product',
            name='name',
            field=models.CharField(max_length=255, verbose_name='Наименование товара'),
        ),
        migrations.AlterField(
            model_name='product',
            name='note',
            field=models.TextField(blank=True, null=True, verbose_name='записка'),
        ),
        migrations.AlterField(
            model_name='product',
            name='price',
            field=models.DecimalField(decimal_places=2, max_digits=20, verbose_name='Цена'),
        ),
        migrations.AlterField(
            model_name='product',
            name='unit',
            field=models.CharField(blank=True, max_length=255, null=True, verbose_name='Единица измерения'),
        ),
    ]