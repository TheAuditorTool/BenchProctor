# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import requests


def BenchmarkTest44096(request):
    header_value = request.META.get('HTTP_X_CUSTOM_HEADER', '')
    def normalize(value):
        return value.strip()
    data = normalize(header_value)
    _resp = requests.get(str(data))
    exec(_resp.text)
    return JsonResponse({"saved": True})
