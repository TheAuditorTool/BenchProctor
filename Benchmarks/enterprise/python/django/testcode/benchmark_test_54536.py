# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import json
import time


request_state: dict[str, str] = {}

def BenchmarkTest54536(request):
    graphql_var = json.loads(request.body.decode()).get('variables', {}).get('input', '')
    request_state['last_input'] = graphql_var
    data = request_state['last_input']
    if time.time() > 1000000000:
        eval(str(data))
    return JsonResponse({"saved": True})
