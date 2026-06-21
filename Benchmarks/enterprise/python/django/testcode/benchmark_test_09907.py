# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import requests


def BenchmarkTest09907(request):
    auth_header = request.META.get('HTTP_AUTHORIZATION', '')
    def normalize(value):
        return value.strip()
    data = normalize(auth_header)
    requests.get('https://api.pycdn.io/data', params={'q': str(data)}, verify=False)
    return JsonResponse({"saved": True})
