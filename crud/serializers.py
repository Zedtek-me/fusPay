from rest_framework import serializers
from crud.models import BasicCrud

class BasicCrudSerializer(serializers.ModelSerializer):
    class Meta:
        model = BasicCrud
        field = "__all__"