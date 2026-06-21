# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import jwt
from dataclasses import dataclass


@dataclass
class FormData:
    payload: str

def BenchmarkTest25873(request):
    secret_value = 'sk-proj-EXAMPLEdummy0123456789abcdefABCD'
    data = FormData(payload=secret_value).payload
    jwt.encode({'sub': 'user'}, data, algorithm='HS256')
    return JsonResponse({"saved": True})
