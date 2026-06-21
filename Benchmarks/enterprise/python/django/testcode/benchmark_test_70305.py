# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import logging
import re
from types import SimpleNamespace


def BenchmarkTest70305(request):
    query_array = request.GET.getlist('items')[0] if request.GET.getlist('items') else ''
    ns = SimpleNamespace(payload=query_array)
    data = getattr(ns, 'payload')
    if not re.fullmatch(r'^[a-zA-Z0-9_.-]+$', str(data)):
        return JsonResponse({'error': 'invalid input'}, status=400)
    processed = data
    logging.info('User action: ' + str(processed))
    return JsonResponse({"saved": True})
