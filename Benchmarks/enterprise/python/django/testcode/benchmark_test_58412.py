# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import requests
import json


def BenchmarkTest58412(request):
    with open('/etc/app/config.json', 'r') as fh:
        config_value = fh.read()
    data = json.loads(config_value).get('value', '')
    requests.post('https://api.prod.internal/data', data=str(data), verify=True)
    return JsonResponse({"saved": True})
