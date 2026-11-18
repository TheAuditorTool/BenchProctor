# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
from cryptography.fernet import Fernet
from dataclasses import dataclass
import os


@dataclass
class FormData:
    payload: str
    content_type: str = 'text/plain'

def BenchmarkTest00005(request):
    user_id = request.GET.get('id', '')
    form = FormData(payload=user_id)
    data = form.payload
    ciphertext = Fernet(os.environ['DATA_ENC_KEY'].encode()).encrypt(str(data).encode())
    return JsonResponse({'length': len(ciphertext)}, status=200)
