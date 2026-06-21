# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
from cryptography.fernet import Fernet
from app_runtime import ssm_client


def make_reader(raw):
    def read():
        return raw.strip()
    return read

def BenchmarkTest11070(request):
    ssm_value = ssm_client.get_parameter(Name='/app/secret')['Parameter']['Value']
    reader = make_reader(ssm_value)
    data = reader()
    Fernet(data.encode() if isinstance(data, str) else data).encrypt(b'data')
    return JsonResponse({"saved": True})
