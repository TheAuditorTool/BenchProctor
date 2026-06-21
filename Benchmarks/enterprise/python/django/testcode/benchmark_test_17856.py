# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
from cryptography.fernet import Fernet
import os


def BenchmarkTest17856(request):
    user_id = request.GET.get('id', '')
    ciphertext = Fernet(os.environ['DATA_ENC_KEY'].encode()).encrypt(str(user_id).encode())
    return JsonResponse({'length': len(ciphertext)}, status=200)
