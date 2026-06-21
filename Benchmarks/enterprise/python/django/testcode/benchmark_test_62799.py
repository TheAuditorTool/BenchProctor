# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import secrets
from dataclasses import dataclass
import os


@dataclass
class FormData:
    payload: str

def BenchmarkTest62799(request):
    env_value = os.environ.get('USER_INPUT', '')
    data = FormData(payload=env_value).payload
    token = secrets.token_hex(32)
    return JsonResponse({'token': str(token)}, status=200)
