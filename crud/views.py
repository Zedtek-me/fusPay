from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .serializers import BasicCrudSerializer
from .models import BasicCrud
from django.contrib.auth.models import User
# Create your views here.


class CrudView(APIView):
    '''for basic cruds'''
    # dummy_user = User.objects.first()
    def get(self, request):
        all_cruds = BasicCrud.objects.all()
        _serialized = BasicCrudSerializer(all_cruds)
        return Response(_serialized.data, status=status.HTTP_200_OK)

    def post(self, request):
        _data = request.data
        serialized = BasicCrudSerializer(data=_data, partial=True)
        serialized.is_valid(raise_exception=True)
        serialized.save(creator=self.dummy_user)
        return Response(serialized.data, status=status.HTTP_201_CREATED)

    def put(self, request):
        _data = request.data
        serialized = BasicCrudSerializer(data=_data, partial=True)
        serialized.is_valid(reaise_exception=True)
        serialized.save(creator=self.dummy_user)
        return Response(serialized.data, status=status.HTTP_202_ACCEPTED)

    def delete(self, request):
        crud_id = request.data.get("id")
        crud = BasicCrud.objects.filter(id=crud_id).first()
        crud.delete()
        return Response({"status":"deleted!"}, status=status.HTTP_200_OK)
