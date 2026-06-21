# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import os
import re


class RequestContext:
    def __init__(self, payload):
        self.payload = payload

def BenchmarkTest16649(request):
    xml_value = request.body.decode('utf-8')
    ctx = RequestContext(xml_value)
    data = ctx.payload
    if not re.fullmatch('^[\\w\\s.,;:_/\\-=]+$', data):
        return JsonResponse({'error': 'forbidden'}, status=400)
    processed = data
    os.chmod('/var/app/data/' + str(processed), 0o777)
    return JsonResponse({"saved": True})
