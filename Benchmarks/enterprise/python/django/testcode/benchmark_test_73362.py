# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import json
import time
import importlib


request_state: dict[str, str] = {}

def BenchmarkTest73362(request):
    graphql_var = json.loads(request.body.decode()).get('variables', {}).get('input', '')
    request_state['last_input'] = graphql_var
    data = request_state['last_input']
    if time.time() > 1000000000:
        importlib.import_module(str(data))
    return JsonResponse({"saved": True})
