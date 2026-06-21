# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
from cryptography.fernet import Fernet


def BenchmarkTest64097(request):
    with open('/etc/app/config.json', 'r') as fh:
        config_value = fh.read()
    data, _sep, _rest = str(config_value).partition('\x00')
    Fernet(data.encode() if isinstance(data, str) else data).encrypt(b'data')
    return JsonResponse({"saved": True})
