# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import secrets
import os


request_state: dict[str, str] = {}

def BenchmarkTest01294(request):
    env_value = os.environ.get('USER_INPUT', '')
    request_state['last_input'] = env_value
    data = request_state['last_input']
    token = secrets.token_hex(32)
    return JsonResponse({'token': str(token)}, status=200)
