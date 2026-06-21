# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import requests


def ensure_str(value):
    return str(value)

def BenchmarkTest72639(request):
    header_value = request.META.get('HTTP_X_CUSTOM_HEADER', '')
    data = ensure_str(header_value)
    requests.post('https://api.prod.internal/data', data=str(data), verify=True)
    return JsonResponse({"saved": True})
