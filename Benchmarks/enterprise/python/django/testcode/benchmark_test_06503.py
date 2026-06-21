# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import requests


def default_blank(value):
    return value if value is not None else ''

def BenchmarkTest06503(request):
    host_value = request.META.get('HTTP_HOST', '')
    data = default_blank(host_value)
    requests.get('https://api.pycdn.io/data', params={'q': str(data)}, verify=True)
    return JsonResponse({"saved": True})
