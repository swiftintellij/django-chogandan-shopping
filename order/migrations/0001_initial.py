# Generated by Django 2.2.7 on 2019-11-11 06:56

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('customer', '0001_initial'),
        ('product', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('quantity', models.IntegerField(verbose_name='수량')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='등록일')),
                ('customer', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='customer.Customer', verbose_name='고객')),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='product.Product', verbose_name='상품')),
            ],
            options={
                'verbose_name': '주문',
                'verbose_name_plural': '주문',
                'db_table': 'order',
            },
        ),
    ]
