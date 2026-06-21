# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import requests


def BenchmarkTest09554(request):
    auth_header = request.META.get('HTTP_AUTHORIZATION', '')
    prefix = ''
    data = prefix + str(auth_header)
    requests.post('https://api.prod.internal/data', data=str(data), verify=True)
    return JsonResponse({"saved": True})
