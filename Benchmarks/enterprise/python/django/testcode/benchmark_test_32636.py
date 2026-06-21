# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse


def BenchmarkTest32636(request):
    with open('/etc/app/config.json', 'r') as fh:
        config_value = fh.read()
    data = f'{config_value:.200s}'
    resp = JsonResponse({'status': 'ok'})
    resp.set_cookie('session', str(data), max_age=86400)
    return resp
