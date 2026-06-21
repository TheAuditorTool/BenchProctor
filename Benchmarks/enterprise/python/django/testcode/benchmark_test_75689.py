# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import requests


def BenchmarkTest75689(request):
    with open('/etc/app/config.json', 'r') as fh:
        config_value = fh.read()
    collected = None
    def on_input(value):
        nonlocal collected
        collected = value
    on_input(config_value)
    data = collected
    requests.post('https://api.prod.internal/data', data=str(data), verify=True)
    return JsonResponse({"saved": True})
