# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import requests


def BenchmarkTest04832(request):
    auth_header = request.META.get('HTTP_AUTHORIZATION', '')
    data = ' '.join(str(auth_header).split())
    requests.post('http://api.prod.internal/data', data=str(data))
    return JsonResponse({"saved": True})
