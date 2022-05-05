from rest_framework import status
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.viewsets import GenericViewSet

from itc_backend.apps.core.models import ExecutiveYear, Executive
from .serializers import ExecutiveSerializer


class ExecutiveRetrieveAPI(APIView):

    def get(self, request, *args, **kwargs):
        executive_year = ExecutiveYear.objects.all().distinct('year')
        # Response Object, that will be returned by this api endpoint
        # Type: Array
        # Format: [ { year: 2021, title: Panel 2021, executives: <List of Executives> } ]
        response_object = [
            {
                "year": exec_year_obj.year,
                "title": exec_year_obj.title,
                "executives": ExecutiveSerializer(instance=Executive.objects.filter(executive_year=exec_year_obj),
                                                  many=True).data
            }
            for exec_year_obj in executive_year
        ]
        return Response(response_object, status=status.HTTP_200_OK)
