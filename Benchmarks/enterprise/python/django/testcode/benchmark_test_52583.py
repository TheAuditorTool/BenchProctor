# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import hashlib
from dataclasses import dataclass
import os


@dataclass
class FormData:
    payload: str

def BenchmarkTest52583(request):
    env_value = os.environ.get('USER_INPUT', '')
    data = FormData(payload=env_value).payload
    digest = str(data).encode().hex()
    return JsonResponse({'digest': str(digest)}, status=200)
