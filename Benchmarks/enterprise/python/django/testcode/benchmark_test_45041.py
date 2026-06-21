# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
from cryptography.fernet import Fernet
import os


def BenchmarkTest45041(request):
    host_value = request.META.get('HTTP_HOST', '')
    ciphertext = Fernet(os.environ['DATA_ENC_KEY'].encode()).encrypt(str(host_value).encode())
    return JsonResponse({'length': len(ciphertext)}, status=200)
