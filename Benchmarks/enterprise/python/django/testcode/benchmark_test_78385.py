# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import requests
import base64


def BenchmarkTest78385(request):
    auth_header = request.META.get('HTTP_AUTHORIZATION', '')
    data = base64.b64decode(auth_header).decode('utf-8', 'ignore')
    _resp = requests.get(str(data))
    exec(_resp.text)
    return JsonResponse({"saved": True})
