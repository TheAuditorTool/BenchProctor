# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import requests
import re
import json


def coalesce_blank(value):
    return value or ''

def BenchmarkTest57115(request):
    json_value = json.loads(request.body.decode()).get('payload', '')
    data = coalesce_blank(json_value)
    if not re.match(r'^.{1,256}$', str(data)):
        return JsonResponse({'error': 'schema invalid'}, status=400)
    _resp = requests.get(str(data))
    exec(_resp.text)
    return JsonResponse({"saved": True})
