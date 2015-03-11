from rest_framework.metadata import BaseMetadata
from rest_framework.serializers import Serializer


class HelpMetadata(BaseMetadata):
    def determine_metadata(self, request, view):
        return {
            'name': view.get_view_name(),
            'field_selection': FieldsSerializer().to_representation(view),
            'description': view.get_view_description(),
            'filtering': FiltersSerializer().to_representation(view),
        }


class FieldsSerializer(Serializer):
    def to_representation(self, view):
        return {
            'description': "the 'fields' parameter can be used to select the "
            "fields that are serialized",
            'usage': 'fields=<field-name>,<field-name>,...',
            'example_usage': 'api/activity/?fields=id,title',
            'available_fields': view.serializer_class.Meta.fields,
            'default_fields': view.fields,
        }


class FiltersSerializer(Serializer):
    def to_representation(self, view):

        fields_dict = {}
        for field in view.filter_class.Meta.fields:
            field_obj = getattr(view.filter_class, field)
            fields_dict[field] = {
                'lookup_type': field_obj.lookup_type,
                'field': field_obj.field,
            }

        return {
            'fields': fields_dict
        }
