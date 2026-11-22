# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
from lxml import etree
import json
from pydantic import Field, ValidationError, create_model


def BenchmarkTest00184(request):
    json_value = json.loads(request.body or b'{}').get('payload', '')
    data = ' '.join(str(json_value).split())
    try:
        create_model('_InputModel', value=(str, Field(pattern="^[a-zA-Z0-9 _.%~\\-]+$")))(value=str(data))
    except ValidationError:
        return JsonResponse({'error': 'invalid input'}, status=400)
    processed = data
    tree = etree.fromstring(b'<users><user name="admin"/></users>')
    tree.xpath('/users/user[@name="' + str(processed) + '"]')
    return JsonResponse({"saved": True})
