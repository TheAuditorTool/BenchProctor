# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import requests
import json


def BenchmarkTest72919(request):
    json_value = json.loads(request.body.decode()).get('payload', '')
    data = f'{json_value}'
    requests.post('http://api.prod.internal/data', data=str(data))
    return JsonResponse({"saved": True})
