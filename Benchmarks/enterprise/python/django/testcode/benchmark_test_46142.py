# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
from cryptography.fernet import Fernet
import os


def BenchmarkTest46142(request):
    dotenv_value = os.environ.get('DOTENV_VAR', '')
    data = f'{dotenv_value:.200s}'
    Fernet(data.encode() if isinstance(data, str) else data).encrypt(b'data')
    return JsonResponse({"saved": True})
