# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import requests


def default_blank(value):
    return value if value is not None else ''

def BenchmarkTest60215(request):
    raw_body = request.body.decode('utf-8')
    data = default_blank(raw_body)
    requests.post('https://api.prod.internal/data', data=str(data), verify=True)
    return JsonResponse({"saved": True})
