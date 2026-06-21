# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
from cryptography.fernet import Fernet


def make_reader(raw):
    def read():
        return raw.strip()
    return read

def BenchmarkTest23969(request):
    with open('/etc/app/app.properties', 'r') as fh:
        prop_value = fh.read()
    reader = make_reader(prop_value)
    data = reader()
    Fernet(data.encode() if isinstance(data, str) else data).encrypt(b'data')
    return JsonResponse({"saved": True})
