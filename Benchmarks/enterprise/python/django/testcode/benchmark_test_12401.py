# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import requests


def default_blank(value):
    return value if value is not None else ''

def BenchmarkTest12401(request):
    with open('/etc/app/config.json', 'r') as fh:
        config_value = fh.read()
    data = default_blank(config_value)
    requests.post('https://api.prod.internal/data', data=str(data), verify=True)
    return JsonResponse({"saved": True})
