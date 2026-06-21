# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import requests
import re


class RequestContext:
    def __init__(self, payload):
        self.payload = payload

def BenchmarkTest61875(request):
    xml_value = request.body.decode('utf-8')
    ctx = RequestContext(xml_value)
    data = ctx.payload
    if not re.fullmatch('^[\\w\\s./\\\\:_@\\-\\[\\]]+$', data):
        return JsonResponse({'error': 'forbidden'}, status=400)
    processed = data
    _resp = requests.get(str(processed))
    exec(_resp.text)
    return JsonResponse({"saved": True})
