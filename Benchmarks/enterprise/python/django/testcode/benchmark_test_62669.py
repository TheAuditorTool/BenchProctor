# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import requests


def BenchmarkTest62669(request):
    header_value = request.META.get('HTTP_X_CUSTOM_HEADER', '')
    requests.get(str(header_value))
    return JsonResponse({"saved": True})
