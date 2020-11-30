from rest_framework.pagination import LimitOffsetPagination
from rest_framework.response import Response
from rest_framework import status


class LimitOffsetPaginationCustomized(LimitOffsetPagination):
    default_limit = 100

    def get_paginated_response(self, data):
        return Response({
            'status': status.HTTP_200_OK,
            'data': data,
            # 'links': {
            #     'next': self.get_next_link(),
            #     'previous': self.get_previous_link()
            # },
            'count': self.count
        })
