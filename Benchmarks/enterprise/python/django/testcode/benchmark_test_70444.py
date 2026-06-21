# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
from cryptography.fernet import Fernet
import os


def relay_value(value):
    return value

def BenchmarkTest70444(request):
    multipart_value = request.POST.get('multipart_field', '')
    data = relay_value(multipart_value)
    ciphertext = Fernet(os.environ['DATA_ENC_KEY'].encode()).encrypt(str(data).encode())
    return JsonResponse({'length': len(ciphertext)}, status=200)
