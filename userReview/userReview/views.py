from rest_framework.generics import ListAPIView
from rest_framework.views import Response
from rest_framework.status import HTTP_200_OK


class ReviewListView(ListAPIView):
    def get(self, request, *args, **kwargs):
        keyword = request.query_params['keyword']
        product_id = request.query_params['product_id']
        user_id = request.query_params['userId']
        return Response(data={}, status=HTTP_200_OK)
