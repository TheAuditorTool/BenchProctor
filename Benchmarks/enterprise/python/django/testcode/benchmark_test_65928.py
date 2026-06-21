# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import requests


def BenchmarkTest65928(request):
    forwarded_ip = request.META.get('HTTP_X_FORWARDED_FOR', '')
    def normalize(value):
        return value.strip()
    data = normalize(forwarded_ip)
    requests.post('https://api.prod.internal/data', data=str(data), verify=True)
    return JsonResponse({"saved": True})
