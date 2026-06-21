# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse


def BenchmarkTest77168(request):
    with open('/etc/app/config.json', 'r') as fh:
        config_value = fh.read()
    parts = []
    for token in str(config_value).split(','):
        parts.append(token.strip())
    data = ','.join(parts)
    resp = JsonResponse({'status': 'ok'})
    resp.set_cookie('session', str(data), max_age=86400)
    return resp
