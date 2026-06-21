# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
from cryptography.fernet import Fernet
import os


def BenchmarkTest45124(request):
    cookie_value = request.COOKIES.get('session_token', '')
    data = '%s' % str(cookie_value)
    key = os.environ['DATA_ENC_KEY'].encode()
    encrypted = Fernet(key).encrypt(str(data).encode()).decode()
    resp = JsonResponse({'status': 'ok'})
    resp.set_cookie('session', encrypted, secure=True, httponly=True, samesite='Strict')
    return resp
