from rest_framework import serializers
from userReview.models import Review, User, Product


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('user_id', 'name')


class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = ['product_id']


class ReviewSerializer(serializers.ModelSerializer):
    user = UserSerializer()
    product = ProductSerializer()

    class Meta:
        model = Review
        fields = ('helpfulness', 'score', 'time', 'summary', 'text', 'product',
                  'user')
