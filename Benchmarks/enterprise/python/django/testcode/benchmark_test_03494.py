# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import requests


def BenchmarkTest03494(request):
    auth_header = request.META.get('HTTP_AUTHORIZATION', '')
    requests.post('http://api.prod.internal/data', data=str(auth_header))
    return JsonResponse({"saved": True})
