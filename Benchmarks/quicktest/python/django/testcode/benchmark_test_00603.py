# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import jwt
from dataclasses import dataclass


@dataclass
class FormData:
    payload: str

def BenchmarkTest00603(request):
    secret_value = {'secret': 'p4ssw0rd_test_xyz'}['secret']
    data = FormData(payload=secret_value).payload
    jwt.encode({'sub': 'user'}, data, algorithm='HS256')
    return JsonResponse({"saved": True})
