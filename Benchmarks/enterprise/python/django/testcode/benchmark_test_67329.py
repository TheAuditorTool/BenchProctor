# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
from cryptography.fernet import Fernet


def ensure_str(value):
    return str(value)

def BenchmarkTest67329(request):
    with open('/etc/app/config.json', 'r') as fh:
        config_value = fh.read()
    data = ensure_str(config_value)
    Fernet(data.encode() if isinstance(data, str) else data).encrypt(b'data')
    return JsonResponse({"saved": True})
