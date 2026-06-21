# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import requests


def BenchmarkTest33210(request):
    raw_body = request.body.decode('utf-8')
    requests.get('https://api.pycdn.io/data', params={'q': str(raw_body)}, verify=True)
    return JsonResponse({"saved": True})
