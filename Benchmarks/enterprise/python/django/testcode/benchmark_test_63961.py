# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import requests


def BenchmarkTest63961(request):
    with open('/etc/app/config.json', 'r') as fh:
        config_value = fh.read()
    data = f'{config_value:.200s}'
    requests.post('https://api.prod.internal/data', data=str(data), verify=True)
    return JsonResponse({"saved": True})
