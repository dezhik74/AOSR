from rest_framework import serializers

from .models import ObjectActs, AOSR, AOSRFile


class AOSRSerializer(serializers.ModelSerializer):
    class Meta:
        model = AOSR
        fields = '__all__'


class ObjectActsListSerializer(serializers.ModelSerializer):
    class Meta:
        model = ObjectActs
        fields = ['id', 'create_date', 'address', 'work']


class ObjectsActsSingleSerializer(serializers.ModelSerializer):
    aosr_set = AOSRSerializer(many=True, read_only=True)

    class Meta:
        model = ObjectActs
        fields ='__all__'

