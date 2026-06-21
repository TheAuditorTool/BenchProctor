# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import requests


def BenchmarkTest20693(request):
    raw_body = request.body.decode('utf-8')
    data = (lambda v: v.strip())(raw_body)
    requests.post('http://api.prod.internal/data', data=str(data))
    return JsonResponse({"saved": True})
