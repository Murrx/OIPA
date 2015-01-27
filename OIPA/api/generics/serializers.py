from rest_framework import serializers
from api.generics import utils
from rest_framework.pagination import PaginationSerializer


class DynamicFields(object):

    @property
    def is_root_dynamic_fields(self):
        """
        Returns true if the current DynamicFields serializer is the root
        DynamicFields serializer.
        """
        parent = self.parent
        root = self.root
        result = None

        if parent is None:
            return True

        while result is None:
            if root == parent or not hasattr(parent, 'parent'):
                result = True
            if isinstance(parent, DynamicFields):
                result = False
            else:
                parent = parent.parent
        return result

    def __init__(self, *args, **kwargs):
        self.query_field = kwargs.pop('query_field', 'fields')
        self.selected_fields = kwargs.pop('fields', None)
        if self.selected_fields is not None:
            self.selected_fields = list(self.selected_fields)
        self.fields_selected = False
        self.query_select = False

        super(DynamicFields, self).__init__(*args, **kwargs)

    def fields_from_query_params(self, query_params):

        if self.query_field in query_params and self.is_root_dynamic_fields:
            self.selected_fields = query_params[self.query_field].split(',')
            self.query_select = True

        for k, v in query_params.items():
            print k, v
            stack = utils.get_type_stack(k)
            field = self
            for item in stack:
                if isinstance(field, DynamicFields):
                    if field.selected_fields and field.query_select:
                        field.selected_fields.append(item)
                    else:
                        field.selected_fields = [item]
                        field.query_select = True

                field = field.fields[item]
            if field is not self:
                values = v.split(',')
                print values
                field.selected_fields = values
        print self.selected_fields

    def select_fields(self):

        if self.is_root_dynamic_fields:
            query_params = utils.query_params_from_context(self.context)
            view = self.context.get('view')
            if view and self.selected_fields is None:
                fields = getattr(view, 'fields', None)
                if fields:
                    self.selected_fields = list(fields)
            if query_params:
                params = dict(query_params)
                self.fields_from_query_params(params)

        if self.selected_fields is not None:
            keep_fields = set(self.selected_fields)
            all_fields = set(self.fields.keys())
            for field_name in all_fields - keep_fields:
                del self.fields[field_name]

    def to_representation(self, instance):
        if not self.fields_selected:
            self.select_fields()
            self.fields_selected = True
        return super(DynamicFields, self).to_representation(instance)


class DynamicFieldsSerializer(DynamicFields, serializers.Serializer):
    def __init__(self, *args, **kwargs):
        # Instantiate mixin, superclass
        super(DynamicFieldsSerializer, self).__init__(*args, **kwargs)


class DynamicFieldsModelSerializer(DynamicFields, serializers.ModelSerializer):
    def __init__(self, *args, **kwargs):
        # Instantiate mixin, superclass
        super(DynamicFieldsModelSerializer, self).__init__(*args, **kwargs)


class NoCountPaginationSerializer(PaginationSerializer):
    """
    PaginationSerializer that removes the count field when specified in the
    query_params.
    """
    def __init__(self, *args, **kwargs):
        super(NoCountPaginationSerializer, self).__init__(*args, **kwargs)
        query_params = utils.query_params_from_context(self.context)
        if 'nocount' in query_params:
            del self.fields['count']
