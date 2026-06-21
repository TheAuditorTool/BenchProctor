# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
from cryptography.fernet import Fernet
import os
import ast


def BenchmarkTest05694(request):
    env_value = os.environ.get('USER_INPUT', '')
    try:
        data = str(ast.literal_eval(env_value))
    except (ValueError, SyntaxError):
        data = env_value
    ciphertext = Fernet(os.environ['DATA_ENC_KEY'].encode()).encrypt(str(data).encode())
    return JsonResponse({'length': len(ciphertext)}, status=200)
