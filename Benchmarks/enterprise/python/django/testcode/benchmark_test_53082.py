# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
from types import SimpleNamespace


def BenchmarkTest53082(request):
    with open('/etc/app/config.json', 'r') as fh:
        config_value = fh.read()
    ns = SimpleNamespace(payload=config_value)
    data = getattr(ns, 'payload')
    processed = data[:64]
    resp = JsonResponse({'status': 'ok'})
    resp.set_cookie('session', str(processed), max_age=86400)
    return resp
