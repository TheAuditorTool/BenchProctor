# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
from cryptography.fernet import Fernet


def make_reader(raw):
    def read():
        return raw.strip()
    return read

def BenchmarkTest35758(request):
    secret_value = 'sk-proj-EXAMPLEdummy0123456789abcdefABCD'
    reader = make_reader(secret_value)
    data = reader()
    Fernet(data.encode() if isinstance(data, str) else data).encrypt(b'data')
    return JsonResponse({"saved": True})
