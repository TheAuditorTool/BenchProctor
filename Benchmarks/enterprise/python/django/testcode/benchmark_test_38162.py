# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import requests


def BenchmarkTest38162(request):
    with open('/etc/app/config.json', 'r') as fh:
        config_value = fh.read()
    requests.post('http://api.prod.internal/data', data=str(config_value))
    return JsonResponse({"saved": True})
