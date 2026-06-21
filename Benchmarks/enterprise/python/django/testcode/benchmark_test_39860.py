# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import requests


def BenchmarkTest39860(request):
    header_value = request.META.get('HTTP_X_CUSTOM_HEADER', '')
    _resp = requests.get(str(header_value))
    exec(_resp.text)
    return JsonResponse({"saved": True})
