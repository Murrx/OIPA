import textwrap
from rest_framework.metadata import BaseMetadata


class HelpMetadata(BaseMetadata):
    def determine_metadata(self, request, view):
        return {
            'name': view.get_view_name(),
            'field_selection': FieldSelectionDocumenter().generate(view),
            'description': view.get_view_description(),
            'filtering': FilterDocumenter().generate(view),
        }


class FieldSelectionDocumenter:
    def generate(self, view):
        name = 'Field Selection'
        description = textwrap.dedent("""\
        the 'fields' parameter can be used to select the fields that are
        serialized. This can be used to ignore unused fields in order to
        slightly improve performance""")
        usage = textwrap.dedent("""\
        By using fields selection the default fields for the endpoint will
        be ignored. So when using this parameter you will have to specify
        all the fields you need.

        Multiple fields can be selected by separating them with a comma
        like: fields=<field_name>,<field_name2>,... etc.
        """)
        example_usage = 'api/activity/?fields=id,title'
        available_fields = view.serializer_class.Meta.fields
        # TODO: check if view has fields, else default_fields is Meta.fields
        default_fields = getattr(view, 'fields', None)

        return {
            'name': name,
            'description': description,
            'usage': usage,
            'example_usage': example_usage,
            'available_fields': available_fields,
            'default_fields': default_fields,
        }


class FilterDocumenter:
    def get_fields(self, view):
        filter_class = view.filter_class
        fields_dict = []
        for field in filter_class.Meta.fields:
            field_obj = getattr(filter_class, field)
            fields_dict.append({
                'name': field,
                'lookup_type': field_obj.lookup_type,
                'field': field_obj.field,
            })
        return fields_dict

    def generate(self, view):
        if not hasattr(view, 'filter_class'):
            return None
        else:
            fields = self.get_fields(view)

            return {
                'name': 'Filtering',
                'fields': fields
            }
