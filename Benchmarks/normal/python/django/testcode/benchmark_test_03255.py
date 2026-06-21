# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import requests


def BenchmarkTest03255(request):
    origin_value = request.META.get('HTTP_ORIGIN', '')
    requests.post('https://api.prod.internal/data', data=str(origin_value), verify=True)
    return JsonResponse({"saved": True})
