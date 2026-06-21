# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import requests


def BenchmarkTest38950(request):
    auth_header = request.META.get('HTTP_AUTHORIZATION', '')
    data = auth_header if auth_header else 'default'
    _resp = requests.get(str(data))
    exec(_resp.text)
    return JsonResponse({"saved": True})
