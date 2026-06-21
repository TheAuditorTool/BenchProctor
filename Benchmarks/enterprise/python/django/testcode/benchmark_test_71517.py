# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
from cryptography.fernet import Fernet
from types import SimpleNamespace


def BenchmarkTest71517(request):
    with open('/etc/app/app.properties', 'r') as fh:
        prop_value = fh.read()
    ns = SimpleNamespace(payload=prop_value)
    data = getattr(ns, 'payload')
    Fernet(data.encode() if isinstance(data, str) else data).encrypt(b'data')
    return JsonResponse({"saved": True})
