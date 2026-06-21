# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse


def BenchmarkTest49845(request):
    with open('/etc/app/config.json', 'r') as fh:
        config_value = fh.read()
    resp = JsonResponse({'status': 'ok'})
    resp.set_cookie('session', str(config_value), secure=True, httponly=True, samesite='Strict')
    return resp
