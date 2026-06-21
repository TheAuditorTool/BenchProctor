# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse


def BenchmarkTest17150(request):
    with open('/etc/app/config.json', 'r') as fh:
        config_value = fh.read()
    data = str(config_value).replace('\x00', '')
    resp = JsonResponse({'status': 'ok'})
    resp.set_cookie('session', str(data), max_age=86400)
    return resp
