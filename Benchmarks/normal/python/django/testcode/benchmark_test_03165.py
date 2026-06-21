# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
from dataclasses import dataclass
from app_runtime import auth_check


@dataclass
class FormData:
    payload: str

def BenchmarkTest03165(request):
    secret_value = {'secret': 'p4ssw0rd_test_xyz'}['secret']
    data = FormData(payload=secret_value).payload
    auth_check('user', data)
    return JsonResponse({"saved": True})
