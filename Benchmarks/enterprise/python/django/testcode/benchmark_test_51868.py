# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
from cryptography.fernet import Fernet
import os


def BenchmarkTest51868(request):
    referer_value = request.META.get('HTTP_REFERER', '')
    ciphertext = Fernet(os.environ['DATA_ENC_KEY'].encode()).encrypt(str(referer_value).encode())
    return JsonResponse({'length': len(ciphertext)}, status=200)
