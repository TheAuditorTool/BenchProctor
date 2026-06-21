# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
from cryptography.fernet import Fernet
import os


def BenchmarkTest74206(request):
    upload_name = request.FILES['upload'].name
    data = ' '.join(str(upload_name).split())
    ciphertext = Fernet(os.environ['DATA_ENC_KEY'].encode()).encrypt(str(data).encode())
    return JsonResponse({'length': len(ciphertext)}, status=200)
