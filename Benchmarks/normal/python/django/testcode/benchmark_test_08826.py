# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
from cryptography.fernet import Fernet
from dataclasses import dataclass


@dataclass
class FormData:
    payload: str

def BenchmarkTest08826(request):
    secret_value = {'secret': 'p4ssw0rd_test_xyz'}['secret']
    data = FormData(payload=secret_value).payload
    Fernet(data.encode() if isinstance(data, str) else data).encrypt(b'data')
    return JsonResponse({"saved": True})
