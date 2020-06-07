from rest_framework.generics import ListAPIView, GenericAPIView
from rest_framework.views import Response, Request
from django.shortcuts import render
from rest_framework.status import HTTP_200_OK
from userReview.models import Review, User, Product
from userReview.pagination import CustomPageNumber
from userReview.serializer import ReviewSerializer
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger


def get_highest_review(keyword):
    reviews = Review.objects.filter(text__contains=keyword).order_by("-score").values("userId__profileName",
                                                                                      "userId__userId",
                                                                                      "productId__productId",
                                                                                      "helpfulness",
                                                                                      "score",
                                                                                      "time",
                                                                                      "summary",
                                                                                      "text")

    return reviews


class ReviewListView(ListAPIView):
    queryset = ''
    serializer_class = ReviewSerializer
    pagination_class = CustomPageNumber

    def get(self, request, *args, **kwargs):
        keyword = request.query_params['keyword']
        self.queryset = get_highest_review(keyword=keyword)
        queryset = self.filter_queryset(self.get_queryset())
        # return Response(data=ReviewSerializer(reviews, many=True).data, status=HTTP_200_OK)
        page = self.paginate_queryset(queryset)
        if page is not None:
            serializer = self.get_serializer(page, many=True)
            return self.get_paginated_response(serializer.data)
        serializer = self.get_serializer(queryset, many=True)
        return Response(data=serializer.data, status=HTTP_200_OK)


class HomeAPIView(GenericAPIView):
    def get(self, request: Request, *args, **kwargs): return render(request=request, template_name="index.html")
