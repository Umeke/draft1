# Generated by Django 4.0.5 on 2022-06-19 13:36

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cat_name', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='Shop',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('shop_name', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('product_name', models.CharField(max_length=200)),
                ('cat_name', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='shop.category')),
                ('shop_name', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='shop.shop')),
            ],
        ),
        migrations.AddField(
            model_name='category',
            name='shop_name',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='shop.shop'),
        ),
    ]
