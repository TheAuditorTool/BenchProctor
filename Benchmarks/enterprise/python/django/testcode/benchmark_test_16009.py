# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
from cryptography.fernet import Fernet


def BenchmarkTest16009(request):
    with open('/etc/app/config.yaml', 'r') as fh:
        yaml_value = fh.read()
    prefix = ''
    data = prefix + str(yaml_value)
    Fernet(data.encode() if isinstance(data, str) else data).encrypt(b'data')
    return JsonResponse({"saved": True})
