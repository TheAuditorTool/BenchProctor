# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import logging
from types import SimpleNamespace


def BenchmarkTest54398(request):
    with open('/etc/app/config.yaml', 'r') as fh:
        yaml_value = fh.read()
    ns = SimpleNamespace(payload=yaml_value)
    data = getattr(ns, 'payload')
    logging.info('User action: ' + str(data))
    return JsonResponse({"saved": True})
