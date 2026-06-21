# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import json
import requests


request_state: dict[str, str] = {}

def BenchmarkTest46447(request):
    api_value = requests.get('http://169.254.169.254/latest/meta-data/iam/security-credentials/').text
    request_state['last_input'] = api_value
    data = request_state['last_input']
    json.loads(data)
    return JsonResponse({"saved": True})
