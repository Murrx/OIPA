import textwrap
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
        description = textwrap.dedent("""\
        the 'fields' parameter can be used to select the fields that are
        serialized""")

        return {
            'description': description,
            'usage': 'fields=<field-name>,<field-name>,...',
            'example_usage': 'api/activity/?fields=id,title',
            'available_fields': view.serializer_class.Meta.fields,
            'default_fields': getattr(view, 'fields', None)
        }


class FiltersSerializer(Serializer):
    def to_representation(self, view):

        filter_class = getattr(view, 'filter_class', None)
        fields_dict = {}
        if filter_class:
            for field in filter_class.Meta.fields:
                field_obj = getattr(filter_class, field)
                fields_dict[field] = {
                    'lookup_type': field_obj.lookup_type,
                    'field': field_obj.field,
                }

        return {
            'fields': fields_dict
        }
