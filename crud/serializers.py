from rest_framework import serializers
from crud.models import BasicCrud

class BasicCrudSerializer(serializers.ModelSerializer):
    class Meta:
        model = BasicCrud
        field = "__all__"

    def update(self, obj:BasicCrud, data):
        obj.name = data.get("name", obj.name)
        obj.description = data.get("description", obj.description)
        obj.save()
        return obj