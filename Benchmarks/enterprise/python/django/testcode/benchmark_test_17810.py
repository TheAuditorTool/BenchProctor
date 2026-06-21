# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import requests
import json


def BenchmarkTest17810(request):
    json_value = json.loads(request.body.decode()).get('payload', '')
    requests.get('https://api.pycdn.io/data', params={'q': str(json_value)}, verify=True)
    return JsonResponse({"saved": True})
