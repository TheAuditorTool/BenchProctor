# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
from cryptography.fernet import Fernet
import os


def BenchmarkTest68952(request):
    ua_value = request.META.get('HTTP_USER_AGENT', '')
    if ua_value:
        data = ua_value
    else:
        data = ''
    ciphertext = Fernet(os.environ['DATA_ENC_KEY'].encode()).encrypt(str(data).encode())
    return JsonResponse({'length': len(ciphertext)}, status=200)
