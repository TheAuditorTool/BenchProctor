# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
from dataclasses import dataclass
import os
from app_runtime import auth_check


@dataclass
class FormData:
    payload: str

def BenchmarkTest35990(request):
    env_value = os.environ.get('USER_INPUT', '')
    data = FormData(payload=env_value).payload
    auth_check('user', data)
    return JsonResponse({"saved": True})
