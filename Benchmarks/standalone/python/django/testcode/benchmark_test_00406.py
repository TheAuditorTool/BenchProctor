# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
from lxml import etree
from marshmallow import Schema, fields, validate, ValidationError


def BenchmarkTest00406(request):
    ua_value = request.META.get('HTTP_USER_AGENT', '')
    data, _sep, _rest = str(ua_value).partition('\x00')
    try:
        Schema.from_dict({'value': fields.Str(validate=validate.Regexp("^[a-zA-Z0-9 _.%~\\-]+$"))})().load({'value': str(data)})
    except ValidationError:
        return JsonResponse({'error': 'invalid input'}, status=400)
    processed = data
    tree = etree.fromstring(b'<users><user name="admin"/></users>')
    tree.xpath('/users/user[@name="' + str(processed) + '"]')
    return JsonResponse({"saved": True})
