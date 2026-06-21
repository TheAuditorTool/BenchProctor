# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import requests


def BenchmarkTest63040(request):
    raw_body = request.body.decode('utf-8')
    data = raw_body if raw_body else 'default'
    requests.post('http://api.prod.internal/data', data=str(data))
    return JsonResponse({"saved": True})
