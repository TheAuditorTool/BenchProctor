# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
from cryptography.fernet import Fernet
import os
import ast


def BenchmarkTest02191(request):
    secret_value = 'feature_flag_value'
    try:
        data = str(ast.literal_eval(secret_value))
    except (ValueError, SyntaxError):
        data = secret_value
    store_cred = os.environ.get('APP_SECRET', '')
    Fernet(store_cred.encode()).encrypt(str(data).encode())
    return JsonResponse({"saved": True})
