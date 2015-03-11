from django.shortcuts import render
from api.activity.views import ActivityList as view


def activity_list(request):
    description = "the 'fields' parameter can be used to select the fields that are serialized"
    usage = 'fields=<field-name>,<field-name>,...'
    example_usage = 'api/activity/?fields=id,title'
    available_fields = view.serializer_class.Meta.fields
    default_fields = view.fields

    context = {'description': description, 'usage': usage, 'example_usage': example_usage, 'available_fields': available_fields, 'default_fields': default_fields}
    return render(request, 'rest_framework/docs.html', context)
