# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
from cryptography.fernet import Fernet
from dataclasses import dataclass


@dataclass
class FormData:
    payload: str

def BenchmarkTest23208(request):
    secret_value = 'config_secret_test_abc123'
    data = FormData(payload=secret_value).payload
    Fernet(data.encode() if isinstance(data, str) else data).encrypt(b'data')
    return JsonResponse({"saved": True})
