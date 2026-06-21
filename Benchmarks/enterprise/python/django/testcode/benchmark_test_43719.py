# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import secrets
import json


request_state: dict[str, str] = {}

def BenchmarkTest43719(request):
    graphql_var = json.loads(request.body.decode()).get('variables', {}).get('input', '')
    request_state['last_input'] = graphql_var
    data = request_state['last_input']
    token = secrets.token_hex(32)
    return JsonResponse({'token': str(token)}, status=200)
