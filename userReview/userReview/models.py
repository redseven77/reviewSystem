from django.db import models
from django.db.models import Q


class Product(models.Model):
    product_id = models.CharField(max_length=255, null=False, unique=True)

    class Meta:
        app_label = "userReview"


class User(models.Model):
    user_id = models.CharField(max_length=255, null=False, unique=True)
    name = models.CharField(max_length=255, null=False)
    product = models.ManyToManyField(to=Product, through='Review')

    class Meta:
        app_label = "userReview"


class Review(models.Model):
    user = models.ForeignKey(to=User, on_delete=models.CASCADE)
    product = models.ForeignKey(to=Product, on_delete=models.CASCADE)
    helpfulness = models.CharField(max_length=255)
    score = models.FloatField(max_length=10)
    time = models.CharField(max_length=255, null=False)
    summary = models.TextField(null=False)
    text = models.TextField(null=False)

    class Meta:
        app_label = "userReview"




