# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
from cryptography.fernet import Fernet
from dataclasses import dataclass
import os


@dataclass
class FormData:
    payload: str

def BenchmarkTest65708(request):
    secret_value = 'feature_flag_value'
    data = FormData(payload=secret_value).payload
    Fernet(os.environ['DATA_ENC_KEY'].encode()).encrypt(str(data).encode())
    return JsonResponse({"saved": True})
