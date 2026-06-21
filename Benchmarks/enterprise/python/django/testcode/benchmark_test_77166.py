# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
from cryptography.fernet import Fernet
import json
import os


request_state: dict[str, str] = {}

def BenchmarkTest77166(request):
    json_value = json.loads(request.body.decode()).get('payload', '')
    request_state['last_input'] = json_value
    data = request_state['last_input']
    key = os.environ['DATA_ENC_KEY'].encode()
    globals().setdefault('_secret_cache', {})['current'] = Fernet(key).encrypt(str(data).encode())
    return JsonResponse({"saved": True})
