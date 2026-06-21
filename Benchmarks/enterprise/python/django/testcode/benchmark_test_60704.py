# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import requests


def BenchmarkTest60704(request):
    host_value = request.META.get('HTTP_HOST', '')
    data = host_value if host_value else 'default'
    requests.get(str(data))
    return JsonResponse({"saved": True})
