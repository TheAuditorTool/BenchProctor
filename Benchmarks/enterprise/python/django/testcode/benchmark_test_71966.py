# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import requests


def BenchmarkTest71966(request):
    header_value = request.META.get('HTTP_X_CUSTOM_HEADER', '')
    requests.post('https://api.prod.internal/data', data=str(header_value), verify=True)
    return JsonResponse({"saved": True})
