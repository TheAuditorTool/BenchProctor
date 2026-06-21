# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import json


def BenchmarkTest22247(request):
    json_value = json.loads(request.body.decode()).get('payload', '')
    with open('/var/data/secrets.txt', 'w') as fh:
        fh.write(str(json_value))
    return JsonResponse({"saved": True})
