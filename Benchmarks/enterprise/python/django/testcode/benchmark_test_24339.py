# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import requests


def BenchmarkTest24339(request):
    auth_header = request.META.get('HTTP_AUTHORIZATION', '')
    prefix = ''
    data = prefix + str(auth_header)
    requests.post('http://api.prod.internal/data', data=str(data))
    return JsonResponse({"saved": True})
