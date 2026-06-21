# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import requests


def default_blank(value):
    return value if value is not None else ''

def BenchmarkTest05429(request):
    forwarded_ip = request.META.get('HTTP_X_FORWARDED_FOR', '')
    data = default_blank(forwarded_ip)
    requests.get('https://api.pycdn.io/data', params={'q': str(data)}, verify=False)
    return JsonResponse({"saved": True})
