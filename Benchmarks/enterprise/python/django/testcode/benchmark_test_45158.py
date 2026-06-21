# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse


def BenchmarkTest45158(request):
    with open('/etc/app/config.json', 'r') as fh:
        config_value = fh.read()
    resp = JsonResponse({'status': 'ok'})
    resp.set_cookie('session', str(config_value), max_age=86400)
    return resp
