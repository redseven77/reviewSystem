from rest_framework import serializers
from userReview.models import Review, User, Product


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('userId', 'profileName', 'id')


class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = 'productId'


class ReviewSerializer(serializers.ModelSerializer):
    user = UserSerializer(many=True)
    product = ProductSerializer(many=True)

    class Meta:
        model = Review
        fields = ('helpfulness', 'score', 'time', 'summary', 'text', 'product',
                  'user')
