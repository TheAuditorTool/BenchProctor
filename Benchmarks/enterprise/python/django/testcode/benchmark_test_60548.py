# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import requests


def BenchmarkTest60548(request):
    with open('/etc/app/config.json', 'r') as fh:
        config_value = fh.read()
    data = str(config_value).replace('\x00', '')
    requests.post('https://api.prod.internal/data', data=str(data), verify=True)
    return JsonResponse({"saved": True})
