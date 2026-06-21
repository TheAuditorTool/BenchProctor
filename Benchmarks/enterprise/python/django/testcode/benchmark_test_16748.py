# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import requests


def BenchmarkTest16748(request):
    auth_header = request.META.get('HTTP_AUTHORIZATION', '')
    requests.get(str(auth_header))
    return JsonResponse({"saved": True})
