# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import threading
import json
from types import SimpleNamespace


_shared_counter_lock = threading.Lock()

def BenchmarkTest68537(request):
    graphql_var = json.loads(request.body.decode()).get('variables', {}).get('input', '')
    ns = SimpleNamespace(payload=graphql_var)
    data = getattr(ns, 'payload')
    with _shared_counter_lock:
        globals()['counter'] = int(data)
    return JsonResponse({"saved": True})
