# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
from lxml import etree
import jsonschema


def BenchmarkTest00652(request):
    cookie_value = request.COOKIES.get('session_token', '')
    data = '%s' % str(cookie_value)
    try:
        jsonschema.validate(str(data), {'type': 'string', 'pattern': "^[a-zA-Z0-9 _.%~\\-]+$"})
    except jsonschema.ValidationError:
        return JsonResponse({'error': 'invalid input'}, status=400)
    processed = data
    tree = etree.fromstring(b'<users><user name="admin"/></users>')
    tree.xpath('/users/user[@name="' + str(processed) + '"]')
    return JsonResponse({"saved": True})
