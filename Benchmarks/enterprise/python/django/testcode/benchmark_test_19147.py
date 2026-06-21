# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
from cryptography.fernet import Fernet
import os


def BenchmarkTest19147(request):
    env_value = os.environ.get('USER_INPUT', '')
    data, _sep, _rest = str(env_value).partition('\x00')
    Fernet(data.encode() if isinstance(data, str) else data).encrypt(b'data')
    return JsonResponse({"saved": True})
