from django.db import models


class Shop(models.Model):
    shop_name = models.CharField(max_length=200)

    def __str__(self):
        return self.shop_name


class Category(models.Model):
    shop_name = models.ForeignKey(Shop, on_delete=models.CASCADE)
    cat_name = models.CharField(max_length=200)

    def __str__(self):
        return self.cat_name


class Product(models.Model):
    product_name = models.CharField(max_length=200)
    shop_name = models.ForeignKey(Shop, on_delete=models.CASCADE)
    cat_name = models.ForeignKey(Category, on_delete=models.CASCADE)


    def __str__(self):
        return self.product_name