# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import json


def BenchmarkTest11175(request):
    with open('/etc/app/config.json', 'r') as fh:
        config_value = fh.read()
    try:
        data = json.loads(config_value).get('value', config_value)
    except (json.JSONDecodeError, AttributeError):
        data = config_value
    resp = JsonResponse({'status': 'ok'})
    resp.set_cookie('session', str(data), max_age=86400)
    return resp
