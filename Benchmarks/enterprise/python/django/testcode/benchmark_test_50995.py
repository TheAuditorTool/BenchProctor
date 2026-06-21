# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
from cryptography.fernet import Fernet
import os
from types import SimpleNamespace
from app_runtime import db


def BenchmarkTest50995(request):
    profile_value = db.fetch_one('SELECT bio FROM profiles LIMIT 1')
    ns = SimpleNamespace(payload=profile_value)
    data = getattr(ns, 'payload')
    key = os.environ['DATA_ENC_KEY'].encode()
    encrypted = Fernet(key).encrypt(str(data).encode()).decode()
    resp = JsonResponse({'status': 'ok'})
    resp.set_cookie('session', encrypted, secure=True, httponly=True, samesite='Strict')
    return resp
