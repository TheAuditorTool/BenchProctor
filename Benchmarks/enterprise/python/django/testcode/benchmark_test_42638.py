# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import requests


def to_text(value):
    return str(value).strip()

def BenchmarkTest42638(request):
    host_value = request.META.get('HTTP_HOST', '')
    data = to_text(host_value)
    requests.get('https://api.pycdn.io/data', params={'q': str(data)}, verify=True)
    return JsonResponse({"saved": True})
