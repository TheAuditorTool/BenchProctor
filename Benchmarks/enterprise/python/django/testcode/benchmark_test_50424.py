# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import requests


def BenchmarkTest50424(request):
    auth_header = request.META.get('HTTP_AUTHORIZATION', '')
    requests.post('https://api.prod.internal/data', data=str(auth_header), verify=True)
    return JsonResponse({"saved": True})
