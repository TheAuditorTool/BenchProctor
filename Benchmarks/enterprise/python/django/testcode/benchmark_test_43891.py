# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
from cryptography.fernet import Fernet
import os
from dataclasses import dataclass


@dataclass
class FormData:
    payload: str

def BenchmarkTest43891(request):
    secret_value = 'feature_flag_value'
    data = FormData(payload=secret_value).payload
    store_cred = os.environ.get('APP_SECRET', '')
    Fernet(store_cred.encode()).encrypt(str(data).encode())
    return JsonResponse({"saved": True})
