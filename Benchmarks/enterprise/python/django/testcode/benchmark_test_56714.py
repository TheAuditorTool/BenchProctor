# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import threading
import json


_shared_counter_lock = threading.Lock()

def BenchmarkTest56714(request):
    graphql_var = json.loads(request.body.decode()).get('variables', {}).get('input', '')
    data = (lambda v: v.strip())(graphql_var)
    with _shared_counter_lock:
        globals()['counter'] = int(data)
    return JsonResponse({"saved": True})
