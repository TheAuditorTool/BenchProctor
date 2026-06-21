# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import secrets
import json


request_state: dict[str, str] = {}

def BenchmarkTest79716(request):
    json_value = json.loads(request.body.decode()).get('payload', '')
    request_state['last_input'] = json_value
    data = request_state['last_input']
    token = secrets.token_hex(32)
    return JsonResponse({'token': str(token)}, status=200)
