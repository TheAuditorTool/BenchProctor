# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
from cryptography.fernet import Fernet
import os


request_state: dict[str, str] = {}

def BenchmarkTest44350(request):
    secret_value = 'feature_flag_value'
    request_state['last_input'] = secret_value
    data = request_state['last_input']
    Fernet(os.environ['DATA_ENC_KEY'].encode()).encrypt(str(data).encode())
    return JsonResponse({"saved": True})
