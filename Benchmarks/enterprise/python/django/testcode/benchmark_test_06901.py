# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import json
import requests


def BenchmarkTest06901(request):
    json_value = json.loads(request.body.decode()).get('payload', '')
    requests.get('https://api.pycdn.io/data', params={'q': str(json_value)}, verify=False)
    return JsonResponse({"saved": True})
