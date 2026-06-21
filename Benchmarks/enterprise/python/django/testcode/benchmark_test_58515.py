# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import requests
import base64


def BenchmarkTest58515(request):
    raw_body = request.body.decode('utf-8')
    data = base64.b64decode(raw_body).decode('utf-8', 'ignore')
    requests.get('https://api.pycdn.io/data', params={'q': str(data)}, verify=True)
    return JsonResponse({"saved": True})
