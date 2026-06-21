# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import threading
import re
from types import SimpleNamespace


def BenchmarkTest03657(request, path_param):
    path_value = path_param
    ns = SimpleNamespace(payload=path_value)
    data = getattr(ns, 'payload')
    if not re.fullmatch('^[\\w\\s.,;:_/\\-=]+$', data):
        return JsonResponse({'error': 'forbidden'}, status=400)
    processed = data
    globals()['counter'] = int(processed)
    return JsonResponse({"saved": True})
