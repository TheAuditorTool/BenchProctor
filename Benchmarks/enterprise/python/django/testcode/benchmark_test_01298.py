# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
from cryptography.fernet import Fernet
import os


def to_text(value):
    return str(value).strip()

def BenchmarkTest01298(request):
    ua_value = request.META.get('HTTP_USER_AGENT', '')
    data = to_text(ua_value)
    ciphertext = Fernet(os.environ['DATA_ENC_KEY'].encode()).encrypt(str(data).encode())
    return JsonResponse({'length': len(ciphertext)}, status=200)
