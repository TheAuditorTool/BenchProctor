# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
from cryptography.fernet import Fernet


request_state: dict[str, str] = {}

def BenchmarkTest56421(request):
    with open('/etc/app/config.yaml', 'r') as fh:
        yaml_value = fh.read()
    request_state['last_input'] = yaml_value
    data = request_state['last_input']
    Fernet(data.encode() if isinstance(data, str) else data).encrypt(b'data')
    return JsonResponse({"saved": True})
