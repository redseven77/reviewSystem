from rest_framework.generics import ListAPIView, GenericAPIView
from rest_framework.views import Response, Request
from django.shortcuts import render
from rest_framework.status import HTTP_200_OK
from userReview.models import Review, User, Product
from userReview.serializer import ReviewSerializer, UserSerializer, ProductSerializer


def get_highest_review(keyword):
    reviews = Review.objects.filter(text__contains=keyword).order_by("-score")
    return reviews


class ReviewListView(ListAPIView):
    queryset = ''

    def get(self, request, *args, **kwargs):
        keyword = request.query_params['keyword']
        reviews = get_highest_review(keyword=keyword)
        data = ReviewSerializer(reviews, many=True).data
        return Response(data=ReviewSerializer(reviews, many=True).data, status=HTTP_200_OK)


class HomeAPIView(GenericAPIView):
    def get(self, request: Request, *args, **kwargs): return render(request=request, template_name="index.html")
