# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
from cryptography.fernet import Fernet


def make_reader(raw):
    def read():
        return raw.strip()
    return read

def BenchmarkTest18398(request):
    with open('/tmp/data', 'r') as fh:
        file_value = fh.read()
    reader = make_reader(file_value)
    data = reader()
    Fernet(data.encode() if isinstance(data, str) else data).encrypt(b'data')
    return JsonResponse({"saved": True})
