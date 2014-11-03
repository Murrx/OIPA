import geodata.models
import iati.models
from rest_framework import serializers


class CityDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = geodata.models.City
        fields = ('id', 'geoname_id', 'name', 'ascii_name', 'alt_name',
            'namepar', 'country', 'location'
        )

        
class CityListSerializer(serializers.ModelSerializer):
    class Meta:
        model = geodata.models.City
        fields = ('id', 'name', 'country', 'location')


class RegionListSerializer(serializers.ModelSerializer):
    class Meta:
        model = geodata.models.Region
        fields = ('code', 'name', 'center_longlat')


class RegionDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = geodata.models.Region
        fields = ()


class ActivityListSerializer(serializers.ModelSerializer):
    descriptions = serializers.SlugRelatedField(many=True, slug_field='description')
    titles = serializers.SlugRelatedField(many=True, slug_field='title')

    class Meta:
        model = iati.models.Activity
        fields = ('id','iati_identifier', 'titles', 'descriptions')
