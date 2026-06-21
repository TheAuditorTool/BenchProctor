# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import jwt
from dataclasses import dataclass


@dataclass
class FormData:
    payload: str

def BenchmarkTest02712(request):
    secret_value = ['s3cr3t_key_test_xyz'][0]
    data = FormData(payload=secret_value).payload
    jwt.encode({'sub': 'user'}, data, algorithm='HS256')
    return JsonResponse({"saved": True})
