# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
from dataclasses import dataclass
from app_runtime import auth_check


@dataclass
class FormData:
    payload: str

def BenchmarkTest18011(request):
    secret_value = 'sk-proj-EXAMPLEdummy0123456789abcdefABCD'
    data = FormData(payload=secret_value).payload
    auth_check('user', data)
    return JsonResponse({"saved": True})
