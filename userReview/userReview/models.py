from django.db import models
from django.db.models import Q


class Product(models.Model):
    productId = models.CharField(max_length=255, null=False, unique=True)

    class Meta:
        app_label = "userReview"


class User(models.Model):
    userId = models.CharField(max_length=255, null=False, unique=True)
    profileName = models.CharField(max_length=255, null=False)
    productId = models.ManyToManyField(to=Product, through='Review')

    class Meta:
        app_label = "userReview"


class Review(models.Model):
    userId = models.ForeignKey(to=User, on_delete=models.CASCADE)
    productId = models.ForeignKey(to=Product, on_delete=models.CASCADE)
    helpfulness = models.CharField(max_length=255)
    score = models.FloatField(max_length=10)
    time = models.CharField(max_length=255, null=False)
    summary = models.TextField(null=False)
    text = models.TextField(null=False)

    class Meta:
        app_label = "userReview"




