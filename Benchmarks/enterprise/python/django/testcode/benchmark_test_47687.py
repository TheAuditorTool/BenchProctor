# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import requests


def BenchmarkTest47687(request):
    forwarded_ip = request.META.get('HTTP_X_FORWARDED_FOR', '')
    requests.post('https://api.prod.internal/data', data=str(forwarded_ip), verify=True)
    return JsonResponse({"saved": True})
