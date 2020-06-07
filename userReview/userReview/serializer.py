from rest_framework import serializers
from userReview.models import Review, User, Product


class ReviewSerializer(serializers.ModelSerializer):
    userId__profileName = serializers.RelatedField(read_only=True, source='user.profileName')
    userId = serializers.RelatedField(read_only=True, source='user.userId')
    productId = serializers.RelatedField(read_only=True, source='product.productId')

    class Meta:
        model = Review
        fields = ['helpfulness', 'score', 'time', 'summary', 'text', 'userId__profileName',
                  'productId', 'userId']


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['userId', 'profileName']


class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = ['productId']
