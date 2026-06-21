# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import requests


def coalesce_blank(value):
    return value or ''

def BenchmarkTest56953(request):
    raw_body = request.body.decode('utf-8')
    data = coalesce_blank(raw_body)
    requests.post('http://api.prod.internal/data', data=str(data))
    return JsonResponse({"saved": True})
