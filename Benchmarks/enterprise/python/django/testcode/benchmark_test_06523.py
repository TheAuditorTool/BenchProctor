# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import json
import requests


def BenchmarkTest06523(request):
    json_value = json.loads(request.body.decode()).get('payload', '')
    pending = list(str(json_value).split(','))
    collected = []
    while pending:
        collected.append(pending.pop(0).strip())
    data = ','.join(collected)
    requests.get('https://api.pycdn.io/data', params={'q': str(data)}, verify=False)
    return JsonResponse({"saved": True})
