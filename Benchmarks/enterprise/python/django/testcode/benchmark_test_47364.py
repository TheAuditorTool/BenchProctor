# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import requests


def BenchmarkTest47364(request):
    origin_value = request.META.get('HTTP_ORIGIN', '')
    requests.get(str(origin_value))
    return JsonResponse({"saved": True})
