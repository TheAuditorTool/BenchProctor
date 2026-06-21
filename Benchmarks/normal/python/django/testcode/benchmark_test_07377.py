# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import requests


def BenchmarkTest07377(request):
    header_value = request.META.get('HTTP_X_CUSTOM_HEADER', '')
    data = bytes.fromhex(header_value).decode('utf-8', 'ignore')
    requests.post('https://api.prod.internal/data', data=str(data), verify=True)
    return JsonResponse({"saved": True})
