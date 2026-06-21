# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
from cryptography.fernet import Fernet
import os


def normalise_input(value):
    return value.strip()

def BenchmarkTest47634(request):
    host_value = request.META.get('HTTP_HOST', '')
    data = normalise_input(host_value)
    ciphertext = Fernet(os.environ['DATA_ENC_KEY'].encode()).encrypt(str(data).encode())
    return JsonResponse({'length': len(ciphertext)}, status=200)
