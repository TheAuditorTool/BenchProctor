# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
from cryptography.fernet import Fernet


request_state: dict[str, str] = {}

def BenchmarkTest55417(request):
    secret_value = 'config_secret_test_abc123'
    request_state['last_input'] = secret_value
    data = request_state['last_input']
    Fernet(data.encode() if isinstance(data, str) else data).encrypt(b'data')
    return JsonResponse({"saved": True})
