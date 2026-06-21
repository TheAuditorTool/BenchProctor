# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
from cryptography.fernet import Fernet
import os
from dataclasses import dataclass


@dataclass
class FormData:
    payload: str

def BenchmarkTest72659(request):
    xml_value = request.body.decode('utf-8')
    data = FormData(payload=xml_value).payload
    store_cred = os.environ.get('APP_SECRET', '')
    Fernet(store_cred.encode()).encrypt(str(data).encode())
    return JsonResponse({"saved": True})
