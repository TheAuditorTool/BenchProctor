# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
from cryptography.fernet import Fernet
import os


def BenchmarkTest44916(request):
    auth_header = request.META.get('HTTP_AUTHORIZATION', '')
    ciphertext = Fernet(os.environ['DATA_ENC_KEY'].encode()).encrypt(str(auth_header).encode())
    return JsonResponse({'length': len(ciphertext)}, status=200)
