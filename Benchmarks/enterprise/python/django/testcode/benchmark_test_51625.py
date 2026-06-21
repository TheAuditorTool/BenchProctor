# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import requests


def BenchmarkTest51625(request):
    host_value = request.META.get('HTTP_HOST', '')
    data = f'{host_value:.200s}'
    requests.post('http://api.prod.internal/data', data=str(data))
    return JsonResponse({"saved": True})
