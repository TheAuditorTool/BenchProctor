# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import json


def BenchmarkTest40511(request):
    json_value = json.loads(request.body.decode()).get('payload', '')
    def normalize(value):
        return value.strip()
    data = normalize(json_value)
    with open('/var/data/secrets.txt', 'w') as fh:
        fh.write(str(data))
    return JsonResponse({"saved": True})
