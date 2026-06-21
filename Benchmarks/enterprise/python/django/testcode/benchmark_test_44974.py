# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import json


def relay_value(value):
    return value

def BenchmarkTest44974(request):
    json_value = json.loads(request.body.decode()).get('payload', '')
    data = relay_value(json_value)
    with open('/var/data/secrets.txt', 'w') as fh:
        fh.write(str(data))
    return JsonResponse({"saved": True})
