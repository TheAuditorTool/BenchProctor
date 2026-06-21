# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
from cryptography.fernet import Fernet
import os


def BenchmarkTest10607(request):
    header_value = request.META.get('HTTP_X_CUSTOM_HEADER', '')
    ciphertext = Fernet(os.environ['DATA_ENC_KEY'].encode()).encrypt(str(header_value).encode())
    return JsonResponse({'length': len(ciphertext)}, status=200)
