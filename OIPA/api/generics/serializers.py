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
        print self._fields_kwarg
        self.selected_fields = []
        self.fields_selected = False

        super(DynamicFields, self).__init__(*args, **kwargs)

    def fields_from_query_params(self, query_params):

        if self.query_field in query_params:
            self.selected_fields = query_params[self.query_field].split(',')

        for k, v in query_params.items():
            stack = utils.get_type_stack(k)
            field = self
            for item in stack:
                if isinstance(field, DynamicFields):
                    field.selected_fields.append(item)

                field = field.fields[item]
            if field is not self:
                values = v.split(',')
                field.selected_fields = values

    def select_fields(self):

        # If we've been here before, skip it.
        if self.fields_selected:
            print "return been here"
            return

        query_params = utils.query_params_from_context(self.context)
        is_top = self.top_dynamic_field is self
        print "is top: " + str(is_top)

        # Retrieve selected_fields from request parameters if the current serializer
        # is the top serializer.
        if is_top and query_params:
            print "istop: queryparams check"
            self.fields_from_query_params(query_params)

        # If serializer has no selected_fields (from query_params) then try:
        print "check selected_fields filled by query " + str(self.selected_fields)
        if not self.selected_fields:
            # Use fields_kwarg if available to determine selected_fields
            print "fields_kwarg: " + str(self._fields_kwarg)
            if self._fields_kwarg:
                self.selected_fields = self._fields_kwarg

            # If there is no fields_kwarg then check the view. This a workaround. Sometimes
            # the fields kwarg can not be specified. For example when
            # ListAPIView is used. The the object_serializer is instantiated DRF itself.
            elif is_top:
                print "from view"
                view = self.context.get('view')
                if view:
                    self.selected_fields = getattr(view, 'fields', None)

        # Actually remove the fields from the serializer.
        # Only do this if selected_fields is filled
        if self.selected_fields or self._fields_kwarg is not None:
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
