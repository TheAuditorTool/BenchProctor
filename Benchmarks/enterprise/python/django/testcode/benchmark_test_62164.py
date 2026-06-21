# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
from cryptography.fernet import Fernet
import os


def BenchmarkTest62164(request):
    origin_value = request.META.get('HTTP_ORIGIN', '')
    ciphertext = Fernet(os.environ['DATA_ENC_KEY'].encode()).encrypt(str(origin_value).encode())
    return JsonResponse({'length': len(ciphertext)}, status=200)
