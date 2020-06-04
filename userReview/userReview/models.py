from django.db import models


class Product(models.Model):
    productId = models.CharField(max_length=255, null=False)


class User(models.Model):
    userId = models.CharField(max_length=255, null=False)
    profileName = models.CharField(max_length=255, null=False)
    productId = models.ManyToManyField(to=Product, through='Review')


class Review(models.Model):
    userId = models.ForeignKey(to=User, on_delete=models.CASCADE)
    productId = models.ForeignKey(to=Product, on_delete=models.CASCADE)
    helpfulness = models.TextField(max_length=255)
    score = models.FloatField(max_length=10)
    time = models.TimeField(auto_now_add=True)
    summary = models.CharField(max_length=255, null=False)
    text = models.CharField(max_length=255, null=False)



