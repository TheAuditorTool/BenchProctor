# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import threading
import json


_shared_counter_lock = threading.Lock()

def BenchmarkTest70791(request):
    graphql_var = json.loads(request.body.decode()).get('variables', {}).get('input', '')
    kind = 'json' if str(graphql_var).lstrip().startswith('{') else 'text'
    match kind:
        case 'json':
            parsed = graphql_var
            data = parsed
        case _:
            data = graphql_var
    with _shared_counter_lock:
        globals()['counter'] = int(data)
    return JsonResponse({"saved": True})
