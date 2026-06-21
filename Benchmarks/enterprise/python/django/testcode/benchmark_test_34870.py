# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import json
import pickle


request_state: dict[str, str] = {}

def BenchmarkTest34870(request):
    graphql_var = json.loads(request.body.decode()).get('variables', {}).get('input', '')
    request_state['last_input'] = graphql_var
    data = request_state['last_input']
    processed = data[:64]
    pickle.loads(processed.encode('latin-1'))
    return JsonResponse({"saved": True})
