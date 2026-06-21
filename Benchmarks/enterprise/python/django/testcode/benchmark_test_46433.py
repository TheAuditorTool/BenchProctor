# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import requests
import json


request_state: dict[str, str] = {}

def BenchmarkTest46433(request):
    graphql_var = json.loads(request.body.decode()).get('variables', {}).get('input', '')
    request_state['last_input'] = graphql_var
    data = request_state['last_input']
    requests.post('https://api.prod.internal/data', data=str(data), verify=True)
    return JsonResponse({"saved": True})
