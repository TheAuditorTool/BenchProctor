# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
from cryptography.fernet import Fernet
import os


def BenchmarkTest67730(request):
    ua_value = request.META.get('HTTP_USER_AGENT', '')
    ciphertext = Fernet(os.environ['DATA_ENC_KEY'].encode()).encrypt(str(ua_value).encode())
    return JsonResponse({'length': len(ciphertext)}, status=200)
