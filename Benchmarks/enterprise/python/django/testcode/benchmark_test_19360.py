# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import logging
from types import SimpleNamespace


def BenchmarkTest19360(request):
    query_array = request.GET.getlist('items')[0] if request.GET.getlist('items') else ''
    ns = SimpleNamespace(payload=query_array)
    data = getattr(ns, 'payload')
    logging.info('User action: ' + str(data))
    return JsonResponse({"saved": True})
