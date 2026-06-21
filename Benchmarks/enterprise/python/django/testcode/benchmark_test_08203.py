# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
from cryptography.fernet import Fernet
import os


def BenchmarkTest08203(request):
    dotenv_value = os.environ.get('DOTENV_VAR', '')
    prefix = ''
    data = prefix + str(dotenv_value)
    Fernet(data.encode() if isinstance(data, str) else data).encrypt(b'data')
    return JsonResponse({"saved": True})
