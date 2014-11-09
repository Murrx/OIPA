import geodata.models
import iati.models
from rest_framework import serializers
from rest_framework.reverse import reverse


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


class RegionListSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = geodata.models.Region
        fields = ('code', 'url', 'name')


class RegionDetailSerializer(serializers.ModelSerializer):
    activity_count = serializers.CharField(source='code', read_only=True)
    class Meta:
        model = geodata.models.Region
        fields = ()

    def transform_activity_count(self, obj, value):
        # Replace with hostname:
        return 'http://localhost:8000' + reverse('region-activity-count', args=(value,))

class RegionActivityCountSerializer(serializers.Serializer):
    activity_count = serializers.CharField(read_only=True)
    class Meta:
        fields = ()


class ActivityListSerializer(serializers.ModelSerializer):
    descriptions = serializers.SlugRelatedField(many=True, slug_field='description')
    titles = serializers.SlugRelatedField(many=True, slug_field='title')

    class Meta:
        model = iati.models.Activity
        fields = ('id','iati_identifier', 'titles', 'descriptions')


class ActivityDetailSerializer(ActivityListSerializer):
    sector = serializers.SlugRelatedField(many=True, slug_field='name')
    class Meta:
        model = iati.models.Activity
        fields = ()
