# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
from lxml import etree
import json
import re


def BenchmarkTest00052(request):
    json_value = json.loads(request.body or b'{}').get('payload', '')
    try:
        data = json.loads(json_value).get('value', json_value)
    except (json.JSONDecodeError, AttributeError):
        data = json_value
    if not re.fullmatch("^(asc|desc|name|created)$", str(data)):
        return JsonResponse({'error': 'forbidden'}, status=400)
    processed = data
    tree = etree.fromstring(b'<users><user name="admin"/></users>')
    tree.xpath('/users/user[@name="' + str(processed) + '"]')
    return JsonResponse({"saved": True})
