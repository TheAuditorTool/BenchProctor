# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import requests
import json


def BenchmarkTest34158(request):
    raw_body = request.body.decode('utf-8')
    data = json.loads(raw_body).get('value', '')
    requests.post('http://api.prod.internal/data', data=str(data))
    return JsonResponse({"saved": True})
