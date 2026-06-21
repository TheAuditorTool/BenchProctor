# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
from cryptography.fernet import Fernet
import os


def BenchmarkTest05851(request):
    dotenv_value = os.environ.get('DOTENV_VAR', '')
    Fernet(dotenv_value.encode() if isinstance(dotenv_value, str) else dotenv_value).encrypt(b'data')
    return JsonResponse({"saved": True})
