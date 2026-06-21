# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
from cryptography.fernet import Fernet


def make_reader(raw):
    def read():
        return raw.strip()
    return read

def BenchmarkTest07839(request):
    with open('/etc/app/config.yaml', 'r') as fh:
        yaml_value = fh.read()
    reader = make_reader(yaml_value)
    data = reader()
    Fernet(data.encode() if isinstance(data, str) else data).encrypt(b'data')
    return JsonResponse({"saved": True})
