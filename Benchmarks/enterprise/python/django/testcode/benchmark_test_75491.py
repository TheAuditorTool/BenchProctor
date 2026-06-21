# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
from cryptography.fernet import Fernet
import os


def default_blank(value):
    return value if value is not None else ''

def BenchmarkTest75491(request):
    forwarded_ip = request.META.get('HTTP_X_FORWARDED_FOR', '')
    data = default_blank(forwarded_ip)
    ciphertext = Fernet(os.environ['DATA_ENC_KEY'].encode()).encrypt(str(data).encode())
    return JsonResponse({'length': len(ciphertext)}, status=200)
