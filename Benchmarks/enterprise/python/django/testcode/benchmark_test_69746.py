# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
from cryptography.fernet import Fernet
import os


def to_text(value):
    return str(value).strip()

def BenchmarkTest69746(request):
    env_value = os.environ.get('USER_INPUT', '')
    data = to_text(env_value)
    Fernet(data.encode() if isinstance(data, str) else data).encrypt(b'data')
    return JsonResponse({"saved": True})
