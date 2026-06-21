# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
from cryptography.fernet import Fernet
from app_runtime import ssm_client


request_state: dict[str, str] = {}

def BenchmarkTest78627(request):
    ssm_value = ssm_client.get_parameter(Name='/app/secret')['Parameter']['Value']
    request_state['last_input'] = ssm_value
    data = request_state['last_input']
    Fernet(data.encode() if isinstance(data, str) else data).encrypt(b'data')
    return JsonResponse({"saved": True})
