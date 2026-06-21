# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import json


def default_blank(value):
    return value if value is not None else ''

def BenchmarkTest07061(request):
    json_value = json.loads(request.body.decode()).get('payload', '')
    data = default_blank(json_value)
    with open('/var/data/secrets.txt', 'w') as fh:
        fh.write(str(data))
    return JsonResponse({"saved": True})
