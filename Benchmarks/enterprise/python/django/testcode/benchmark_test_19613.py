# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import secrets
from dataclasses import dataclass


@dataclass
class FormData:
    payload: str

def BenchmarkTest19613(request, path_param):
    path_value = path_param
    data = FormData(payload=path_value).payload
    token = secrets.token_hex(32)
    return JsonResponse({'token': str(token)}, status=200)
