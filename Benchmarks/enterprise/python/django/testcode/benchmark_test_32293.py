# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import hashlib
import os


request_state: dict[str, str] = {}

def BenchmarkTest32293(request):
    env_value = os.environ.get('USER_INPUT', '')
    request_state['last_input'] = env_value
    data = request_state['last_input']
    digest = str(data).encode().hex()
    return JsonResponse({'digest': str(digest)}, status=200)
