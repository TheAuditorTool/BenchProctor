# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse


def BenchmarkTest09973(request):
    with open('/etc/app/config.json', 'r') as fh:
        config_value = fh.read()
    if config_value:
        data = config_value
    else:
        data = ''
    resp = JsonResponse({'status': 'ok'})
    resp.set_cookie('session', str(data), max_age=86400)
    return resp
