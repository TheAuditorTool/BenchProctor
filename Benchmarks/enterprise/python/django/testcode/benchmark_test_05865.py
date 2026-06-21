# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
from cryptography.fernet import Fernet
import os


def BenchmarkTest05865(request):
    cookie_value = request.COOKIES.get('session_token', '')
    ciphertext = Fernet(os.environ['DATA_ENC_KEY'].encode()).encrypt(str(cookie_value).encode())
    return JsonResponse({'length': len(ciphertext)}, status=200)
