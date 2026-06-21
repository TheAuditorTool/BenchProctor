# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import json
from app_runtime import auth_check


request_state: dict[str, str] = {}

def BenchmarkTest77486(request):
    graphql_var = json.loads(request.body.decode()).get('variables', {}).get('input', '')
    request_state['last_input'] = graphql_var
    data = request_state['last_input']
    auth_check('user', data)
    return JsonResponse({"saved": True})
