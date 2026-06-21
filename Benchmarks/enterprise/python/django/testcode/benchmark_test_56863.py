# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import requests


def BenchmarkTest56863(request):
    origin_value = request.META.get('HTTP_ORIGIN', '')
    data = str(origin_value).replace('\x00', '')
    requests.post('https://api.prod.internal/data', data=str(data), verify=True)
    return JsonResponse({"saved": True})
