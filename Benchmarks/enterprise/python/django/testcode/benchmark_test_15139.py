# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
from cryptography.fernet import Fernet
import os


def BenchmarkTest15139(request):
    user_id = request.GET.get('id', '')
    parts = []
    for token in str(user_id).split(','):
        parts.append(token.strip())
    data = ','.join(parts)
    ciphertext = Fernet(os.environ['DATA_ENC_KEY'].encode()).encrypt(str(data).encode())
    return JsonResponse({'length': len(ciphertext)}, status=200)
