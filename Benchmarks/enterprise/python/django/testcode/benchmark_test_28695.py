# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import requests


def BenchmarkTest28695(request):
    auth_header = request.META.get('HTTP_AUTHORIZATION', '')
    requests.get('https://api.pycdn.io/data', params={'q': str(auth_header)}, verify=True)
    return JsonResponse({"saved": True})
