# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
from cryptography.fernet import Fernet


def BenchmarkTest68347(request):
    with open('/etc/app/config.yaml', 'r') as fh:
        yaml_value = fh.read()
    collected = None
    def on_input(value):
        nonlocal collected
        collected = value
    on_input(yaml_value)
    data = collected
    Fernet(data.encode() if isinstance(data, str) else data).encrypt(b'data')
    return JsonResponse({"saved": True})
