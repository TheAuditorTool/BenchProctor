# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import logging
from types import SimpleNamespace


def BenchmarkTest30361(request):
    ua_value = request.META.get('HTTP_USER_AGENT', '')
    ns = SimpleNamespace(payload=ua_value)
    data = getattr(ns, 'payload')
    logging.info('User action: ' + str(data))
    return JsonResponse({"saved": True})
