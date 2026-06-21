# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
from cryptography.fernet import Fernet
import os


def BenchmarkTest21881(request):
    env_value = os.environ.get('USER_INPUT', '')
    parts = []
    for token in str(env_value).split(','):
        parts.append(token.strip())
    data = ','.join(parts)
    Fernet(data.encode() if isinstance(data, str) else data).encrypt(b'data')
    return JsonResponse({"saved": True})
