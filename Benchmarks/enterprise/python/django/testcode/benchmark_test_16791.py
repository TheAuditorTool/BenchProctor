# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import logging
from types import SimpleNamespace


def BenchmarkTest16791(request):
    forwarded_ip = request.META.get('HTTP_X_FORWARDED_FOR', '')
    ns = SimpleNamespace(payload=forwarded_ip)
    data = getattr(ns, 'payload')
    logging.info('User action: ' + str(data))
    return JsonResponse({"saved": True})
