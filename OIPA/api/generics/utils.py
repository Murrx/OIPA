import re


def parameter_from_type_query_param(query_param):
    """Returns type name from query_param string."""
    regex = r'\[(.*)\]$'
    print query_param
    result = re.search(regex, query_param).group(1)
    print result
    return result


def query_params_from_context(context):
    """Returns query_params dict from context."""
    query_params = None
    try:
        query_params = context['request'].query_params
    except (KeyError, AttributeError):
        pass
    return query_params


def get_type_stack(type_string):
    current = type_string
    result = []

    while True:

        if '[' in type_string:
            type_string = parameter_from_type_query_param(type_string)
        else:
            break

        c = type_string.rsplit('[', 1)[0]
        result.append(c)

    return result


def get_type_parameters(name, query_params):
    """
    Returns query_params dict filtered by type.
    """
    result_fields = {}
    fields_dict = {k: v for k, v in query_params.items()
                   if k.startswith(name)}

    for type_name, type_value in fields_dict.items():
        if '[' in type_name:
            type_name = parameter_from_type_query_param(k)
        result_fields[type_name] = type_value

    return result_fields
