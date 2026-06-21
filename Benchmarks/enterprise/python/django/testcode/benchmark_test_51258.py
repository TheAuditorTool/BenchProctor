# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
from dataclasses import dataclass
from app_runtime import auth_check


@dataclass
class FormData:
    payload: str

def BenchmarkTest51258(request):
    secret_value = 'config_secret_test_abc123'
    data = FormData(payload=secret_value).payload
    auth_check('user', data)
    return JsonResponse({"saved": True})
