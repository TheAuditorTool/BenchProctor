# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import requests


def BenchmarkTest41678(request):
    raw_body = request.body.decode('utf-8')
    data = raw_body if raw_body else 'default'
    requests.post('https://api.prod.internal/data', data=str(data), verify=True)
    return JsonResponse({"saved": True})
