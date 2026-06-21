# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import logging
from types import SimpleNamespace


def BenchmarkTest49947(request):
    with open('/etc/app/app.properties', 'r') as fh:
        prop_value = fh.read()
    ns = SimpleNamespace(payload=prop_value)
    data = getattr(ns, 'payload')
    logging.info('User action: ' + str(data))
    return JsonResponse({"saved": True})
