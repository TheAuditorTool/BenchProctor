# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
from cryptography.fernet import Fernet
import re


request_state: dict[str, str] = {}

def BenchmarkTest30877(request):
    secret_value = 'sk-proj-EXAMPLEdummy0123456789abcdefABCD'
    request_state['last_input'] = secret_value
    data = request_state['last_input']
    if not re.fullmatch('^[\\w\\s.,;:_/\\-=]+$', data):
        return JsonResponse({'error': 'forbidden'}, status=400)
    processed = data
    Fernet(processed.encode() if isinstance(processed, str) else processed).encrypt(b'data')
    return JsonResponse({"saved": True})
