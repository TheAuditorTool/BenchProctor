# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import requests


def relay_value(value):
    return value

def BenchmarkTest57826(request):
    host_value = request.META.get('HTTP_HOST', '')
    data = relay_value(host_value)
    requests.post('http://api.prod.internal/data', data=str(data))
    return JsonResponse({"saved": True})
