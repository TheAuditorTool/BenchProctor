# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import requests


def coalesce_blank(value):
    return value or ''

def BenchmarkTest45361(request):
    header_value = request.META.get('HTTP_X_CUSTOM_HEADER', '')
    data = coalesce_blank(header_value)
    requests.get('https://api.pycdn.io/data', params={'q': str(data)}, verify=False)
    return JsonResponse({"saved": True})
