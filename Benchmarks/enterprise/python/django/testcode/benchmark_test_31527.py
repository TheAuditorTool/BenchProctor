# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
from cryptography.fernet import Fernet
import os


def BenchmarkTest31527(request):
    dotenv_value = os.environ.get('DOTENV_VAR', '')
    data = (lambda v: v.strip())(dotenv_value)
    store_cred = os.environ.get('APP_SECRET', '')
    Fernet(store_cred.encode()).encrypt(str(data).encode())
    return JsonResponse({"saved": True})
