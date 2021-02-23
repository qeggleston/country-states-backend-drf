from rest_framework import serializers
from api.models import Country, State, City

class CountrySerializer(serializers.ModelSerializer):
    class Meta:
        model = Country
        fields = ['id', 'code', 'name']

class CitySerializer(serializers.ModelSerializer):
    class Meta:
        model = City
        fields = ['id', 'name']

class StateSerializer(serializers.ModelSerializer):
    city_set = serializers.HyperlinkedRelatedField(many=True, read_only=True, view_name='city-detail')
    class Meta:
        model = State
        fields = ['id', 'code', 'name', 'country', 'city_set']
