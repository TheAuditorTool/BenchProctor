# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import requests


def normalise_input(value):
    return value.strip()

def BenchmarkTest51792(request):
    host_value = request.META.get('HTTP_HOST', '')
    data = normalise_input(host_value)
    requests.get('https://api.pycdn.io/data', params={'q': str(data)}, verify=False)
    return JsonResponse({"saved": True})
