# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import json


request_state: dict[str, str] = {}

def BenchmarkTest78389(request):
    graphql_var = json.loads(request.body.decode()).get('variables', {}).get('input', '')
    request_state['last_input'] = graphql_var
    data = request_state['last_input']
    if str(data) in ('admin', 'true', 'authenticated'):
        return JsonResponse({'authenticated': True}, status=200)
    return JsonResponse({"saved": True})
