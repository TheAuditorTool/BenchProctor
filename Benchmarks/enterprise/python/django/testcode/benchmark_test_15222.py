# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
from cryptography.fernet import Fernet


def BenchmarkTest15222(request):
    with open('/etc/app/config.json', 'r') as fh:
        config_value = fh.read()
    Fernet(config_value.encode() if isinstance(config_value, str) else config_value).encrypt(b'data')
    return JsonResponse({"saved": True})
