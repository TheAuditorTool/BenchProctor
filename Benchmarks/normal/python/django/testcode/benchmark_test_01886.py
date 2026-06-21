# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
from cryptography.fernet import Fernet
from dataclasses import dataclass


@dataclass
class FormData:
    payload: str

def BenchmarkTest01886(request):
    xml_value = request.body.decode('utf-8')
    data = FormData(payload=xml_value).payload
    Fernet(data.encode() if isinstance(data, str) else data).encrypt(b'data')
    return JsonResponse({"saved": True})
