# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
from cryptography.fernet import Fernet


def BenchmarkTest78125(request):
    with open('/etc/app/config.json', 'r') as fh:
        config_value = fh.read()
    data = config_value if config_value else 'default'
    Fernet(data.encode() if isinstance(data, str) else data).encrypt(b'data')
    return JsonResponse({"saved": True})
