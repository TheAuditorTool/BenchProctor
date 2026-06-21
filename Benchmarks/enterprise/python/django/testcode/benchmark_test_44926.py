# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
from cryptography.fernet import Fernet
import os


def relay_value(value):
    return value

def BenchmarkTest44926(request):
    dotenv_value = os.environ.get('DOTENV_VAR', '')
    data = relay_value(dotenv_value)
    Fernet(data.encode() if isinstance(data, str) else data).encrypt(b'data')
    return JsonResponse({"saved": True})
