# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
from cryptography.fernet import Fernet
import os


def BenchmarkTest69813(request):
    upload_name = request.FILES['upload'].name
    ciphertext = Fernet(os.environ['DATA_ENC_KEY'].encode()).encrypt(str(upload_name).encode())
    return JsonResponse({'length': len(ciphertext)}, status=200)
