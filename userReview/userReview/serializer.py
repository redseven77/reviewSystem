from rest_framework import serializers
from userReview.models import Review, User, Product


class ReviewSerializer(serializers.ModelSerializer):
    user = serializers.RelatedField(source='user', read_only=True)
    # userId = serializers.RelatedField(source='user', read_only=True)
    product_id = serializers.RelatedField(source='product', read_only=True)

    class Meta:
        model = Review
        fields = ['id', 'title', 'code', 'linenos', 'language', 'style']


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['userId', 'profileName']


class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = ['productId']
