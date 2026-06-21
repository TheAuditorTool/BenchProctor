# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import requests


def BenchmarkTest32150(request):
    forwarded_ip = request.META.get('HTTP_X_FORWARDED_FOR', '')
    requests.get('https://api.pycdn.io/data', params={'q': str(forwarded_ip)}, verify=True)
    return JsonResponse({"saved": True})
