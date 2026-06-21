# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
from cryptography.fernet import Fernet
import os


def BenchmarkTest00200(request):
    env_value = os.environ.get('USER_INPUT', '')
    ciphertext = Fernet(os.environ['DATA_ENC_KEY'].encode()).encrypt(str(env_value).encode())
    return JsonResponse({'length': len(ciphertext)}, status=200)
