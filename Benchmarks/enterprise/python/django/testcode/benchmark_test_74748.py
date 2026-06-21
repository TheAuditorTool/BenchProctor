# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import requests


def normalise_input(value):
    return value.strip()

def BenchmarkTest74748(request):
    ua_value = request.META.get('HTTP_USER_AGENT', '')
    data = normalise_input(ua_value)
    requests.post('http://api.prod.internal/data', data=str(data))
    return JsonResponse({"saved": True})
