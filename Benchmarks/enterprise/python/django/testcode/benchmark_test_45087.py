# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
from cryptography.fernet import Fernet


def BenchmarkTest45087(request):
    with open('/etc/app/app.properties', 'r') as fh:
        prop_value = fh.read()
    Fernet(prop_value.encode() if isinstance(prop_value, str) else prop_value).encrypt(b'data')
    return JsonResponse({"saved": True})
