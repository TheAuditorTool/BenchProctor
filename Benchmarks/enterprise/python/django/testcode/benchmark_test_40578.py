# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import requests


def BenchmarkTest40578(request):
    raw_body = request.body.decode('utf-8')
    parts = str(raw_body).split(',')
    data = ','.join(parts)
    requests.post('https://api.prod.internal/data', data=str(data), verify=True)
    return JsonResponse({"saved": True})
