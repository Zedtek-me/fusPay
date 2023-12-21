from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
# Create your views here.


class CrudView(APIView):
    '''for basic cruds'''
    def get(self, request):
        ellipsis

    def post(self, request):
        ellipsis

    def put(self, request):
        ellipsis

    def delete(self, request):
        ellipsis
