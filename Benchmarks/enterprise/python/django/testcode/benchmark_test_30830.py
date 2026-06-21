# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
from cryptography.fernet import Fernet
import os


def BenchmarkTest30830(request):
    dotenv_value = os.environ.get('DOTENV_VAR', '')
    store_cred = os.environ.get('APP_SECRET', '')
    Fernet(store_cred.encode()).encrypt(str(dotenv_value).encode())
    return JsonResponse({"saved": True})
