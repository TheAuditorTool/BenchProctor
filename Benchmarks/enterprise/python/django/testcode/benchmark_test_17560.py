# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import requests


def BenchmarkTest17560(request):
    with open('/etc/app/config.json', 'r') as fh:
        config_value = fh.read()
    data = ' '.join(str(config_value).split())
    requests.post('http://api.prod.internal/data', data=str(data))
    return JsonResponse({"saved": True})
