from rest_framework import serializers
from api.generics import utils
from rest_framework.pagination import PaginationSerializer


class DynamicFields(object):

    @property
    def top_dynamic_field(self):
        """
        Returns the highest (top) DynamicFields serializer.
        """
        current = self
        top = self

        while hasattr(current, 'parent'):
            if isinstance(current, DynamicFields):
                top = current
            current = current.parent

        return top

    def __init__(self, *args, **kwargs):
        self.query_field = kwargs.pop('query_field', 'fields')
        self._fields_kwarg = kwargs.pop('fields', None)
        self.selected_fields = None
        self.fields_selected = False

        super(DynamicFields, self).__init__(*args, **kwargs)

    def sub_fields_query_params(self, query_params):
        for k, v in query_params.items():
            stack = utils.get_type_stack(k)
            field = self
            for item in stack:
                if isinstance(field, DynamicFields):
                    if field.selected_fields is None:
                        field.selected_fields = []
                    field.selected_fields.append(item)

                field = field.fields[item]
            if field is not self:
                values = v.split(',')
                field.selected_fields = values

    def select_fields(self):
        # If we've been here before, skip it.
        if self.selected_fields is not None:
            return

        fields = None
        is_top = self.top_dynamic_field is self

        # Retrieve selected_fields from request parameters if the current serializer
        # is the top serializer.
        if is_top:
            query_params = utils.query_params_from_context(self.context)
            view = self.context.get('view')

            if query_params:
                if self.query_field in query_params:
                    fields = query_params[self.query_field].split(',')
                # DO sub fields
                self.sub_fields_query_params(query_params)

            elif view:
                fields = getattr(view, self.query_field, None)

        if not fields:
            fields = getattr(self, '_fields_kwarg', None)

        if not self.selected_fields:
            self.selected_fields = fields

        if self.selected_fields is not None:
            print "Removing fields, keeping " + str(self.selected_fields)
            keep_fields = set(self.selected_fields)
            print "actual " + str(keep_fields)
            all_fields = set(self.fields.keys())
            for field_name in all_fields - keep_fields:
                del self.fields[field_name]
        self.fields_selected = True

    def to_representation(self, instance):
        self.select_fields()
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
