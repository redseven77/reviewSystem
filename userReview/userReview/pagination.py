from rest_framework import pagination
from rest_framework.views import Response
from collections import OrderedDict


class CustomPageNumber(pagination.PageNumberPagination):
    page_size = 20

    def get_paginated_response(self, data):
        return Response(OrderedDict([
             ('lastPage', self.page.paginator.count),
             ('countItemsOnPage', self.page_size),
             ('current', self.page.number),
             ('next', self.get_next_link()),
             ('previous', self.get_previous_link()),
             ('results', data)
         ]), status=200)
