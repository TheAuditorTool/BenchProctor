# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
from cryptography.fernet import Fernet
import os


def BenchmarkTest06228(request):
    user_id = request.GET.get('id', '')
    collected = None
    def on_input(value):
        nonlocal collected
        collected = value
    on_input(user_id)
    data = collected
    ciphertext = Fernet(os.environ['DATA_ENC_KEY'].encode()).encrypt(str(data).encode())
    return JsonResponse({'length': len(ciphertext)}, status=200)
