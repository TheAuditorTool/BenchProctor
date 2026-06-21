# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
from cryptography.fernet import Fernet
import os


def to_text(value):
    return str(value).strip()

def BenchmarkTest71720(request):
    env_value = os.environ.get('USER_INPUT', '')
    data = to_text(env_value)
    ciphertext = Fernet(os.environ['DATA_ENC_KEY'].encode()).encrypt(str(data).encode())
    return JsonResponse({'length': len(ciphertext)}, status=200)
