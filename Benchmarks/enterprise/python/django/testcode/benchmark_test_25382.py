# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
from cryptography.fernet import Fernet
import os


request_state: dict[str, str] = {}

def BenchmarkTest25382(request):
    secret_value = 'default_config_label'
    request_state['last_input'] = secret_value
    data = request_state['last_input']
    store_cred = os.environ.get('APP_SECRET', '')
    Fernet(store_cred.encode()).encrypt(str(data).encode())
    return JsonResponse({"saved": True})
