# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
from cryptography.fernet import Fernet
import os


def BenchmarkTest10484(request):
    env_value = os.environ.get('USER_INPUT', '')
    Fernet(env_value.encode() if isinstance(env_value, str) else env_value).encrypt(b'data')
    return JsonResponse({"saved": True})
