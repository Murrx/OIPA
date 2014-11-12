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
    related_activity_count = serializers.HyperlinkedIdentityField(view_name='region-activity-count')
    countries_in_region = serializers.HyperlinkedIdentityField(view_name='countries-in-region')
    related_activities = serializers.HyperlinkedIdentityField(view_name='region-related-activities')
    parental_region = serializers.HyperlinkedRelatedField(view_name='region-detail')
    child_regions = serializers.HyperlinkedIdentityField(view_name='child-regions',)
    derived_activities = serializers.HyperlinkedIdentityField(view_name='derived-activities')
    total_activities = serializers.Field()
    class Meta:
        model = geodata.models.Region
        fields = ('code', 'name', 'region_vocabulary', 'center_longlat', 'parental_region', 'countries_in_region', 'related_activity_count', 'related_activities', 'child_regions', 'derived_activities', 'total_activities',)

    def transform_activity_count(self, obj, value):
        pass


class RegionActivityCountSerializer(serializers.Serializer):
    activity_count = serializers.CharField(read_only=True)
    class Meta:
        fields = ()


class ActivityListSerializer(serializers.ModelSerializer):
    url = serializers.HyperlinkedIdentityField(view_name='activity-detail')
    titles = serializers.SlugRelatedField(many=True, slug_field='title')

    class Meta:
        model = iati.models.Activity
        fields = ('id', 'url', 'titles')


class ActivityDetailSerializer(serializers.ModelSerializer):
    sector = serializers.SlugRelatedField(many=True, slug_field='name')
    recipient_countries = serializers.HyperlinkedIdentityField(view_name='activity-recipient-countries')

    class Meta:
        model = iati.models.Activity
        fields = ('id', 'iati_identifier', 'sector', 'recipient_countries', 'default_currency', 'hierarchy', 'last_updated_datetime', 'linked_data_uri', 'reporting_organisation', 'secondary_publisher', 'activity_status', 'start_planned', 'end_planned', 'start_actual', 'end_actual', 'collaboration_type', 'default_flow_type', 'default_aid_type', 'default_finance_type', 'default_tied_status', 'xml_source_ref', 'total_budget_currency', 'total_budget', 'capital_spend', 'scope', 'iati_standard_version', 'participating_organisation', 'policy_marker', 'recipient_region')


class CountryDetailSerializer(serializers.ModelSerializer):
    capital_city = serializers.HyperlinkedRelatedField(view_name='city-detail')
    cities = serializers.HyperlinkedIdentityField(view_name='cities')
    activity_set = serializers.HyperlinkedIdentityField(view_name='activities')
    region = serializers.HyperlinkedRelatedField(view_name='region-detail')
    class Meta:
        model = geodata.models.Country
        fields = ('code', 'name', 'capital_city', 'cities', 'activity_set', 'numerical_code_un', 'alt_name', 'language', 'region', 'un_region', 'unesco_region', 'dac_country_code', 'iso3', 'alpha3', 'fips10', 'center_longlat', 'polygon', 'data_source')


class CountryListSerializer(serializers.ModelSerializer):
    url = serializers.HyperlinkedIdentityField(view_name='country-detail')
    class Meta:
        model = geodata.models.Country
        fields =('code', 'url', 'name', )
