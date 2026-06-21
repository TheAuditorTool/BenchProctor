# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import requests


def BenchmarkTest50436(request):
    with open('/etc/app/config.json', 'r') as fh:
        config_value = fh.read()
    def normalize(value):
        return value.strip()
    data = normalize(config_value)
    requests.post('http://api.prod.internal/data', data=str(data))
    return JsonResponse({"saved": True})
