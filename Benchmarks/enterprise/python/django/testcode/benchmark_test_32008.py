# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import requests
import json


def BenchmarkTest32008(request):
    json_value = json.loads(request.body.decode()).get('payload', '')
    data = f'{json_value:.200s}'
    requests.post('http://api.prod.internal/data', data=str(data))
    return JsonResponse({"saved": True})
