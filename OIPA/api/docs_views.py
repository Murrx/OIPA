import json
import urllib2
from django.shortcuts import render


def activity_list(request, api_call):

    host = request.META['HTTP_HOST']
    call = '{0}{1}'.format(host, api_call)

    handler = urllib2.HTTPHandler()
    opener = urllib2.build_opener(handler)

    req = urllib2.Request('http://{0}'.format(call))
    req.add_header("Content-Type", 'application/json')
    req.get_method = lambda: "OPTIONS"
    try:
        connection = opener.open(req)
    except urllib2.HTTPError, e:
        connection = e
    # check. Substitute with appropriate HTTP code.
    if connection.code == 200:
        data = connection.read()
    else:
        print 'panic!'

    context = json.loads(data)
    context['original_call'] = api_call

    return render(request, 'rest_framework/docs.html', context)
