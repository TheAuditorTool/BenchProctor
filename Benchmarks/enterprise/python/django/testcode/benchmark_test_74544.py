# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse


def BenchmarkTest74544(request):
    with open('/etc/app/config.json', 'r') as fh:
        config_value = fh.read()
    data = (lambda v: v.strip())(config_value)
    resp = JsonResponse({'status': 'ok'})
    resp.set_cookie('session', str(data), max_age=86400)
    return resp
