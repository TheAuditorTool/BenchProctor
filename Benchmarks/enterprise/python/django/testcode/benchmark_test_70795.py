# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
from cryptography.fernet import Fernet
import os


def BenchmarkTest70795(request):
    auth_header = request.META.get('HTTP_AUTHORIZATION', '')
    parts = str(auth_header).split(',')
    data = ','.join(parts)
    key = os.environ['DATA_ENC_KEY'].encode()
    encrypted = Fernet(key).encrypt(str(data).encode()).decode()
    resp = JsonResponse({'status': 'ok'})
    resp.set_cookie('session', encrypted, secure=True, httponly=True, samesite='Strict')
    return resp
