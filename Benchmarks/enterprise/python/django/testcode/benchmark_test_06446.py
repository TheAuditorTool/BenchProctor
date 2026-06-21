# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import threading
import json


_shared_counter_lock = threading.Lock()

def BenchmarkTest06446(request):
    graphql_var = json.loads(request.body.decode()).get('variables', {}).get('input', '')
    if graphql_var:
        data = graphql_var
    else:
        data = ''
    with _shared_counter_lock:
        globals()['counter'] = int(data)
    return JsonResponse({"saved": True})
