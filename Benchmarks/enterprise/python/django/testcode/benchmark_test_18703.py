# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
from cryptography.fernet import Fernet
import os
from types import SimpleNamespace


def BenchmarkTest18703(request):
    secret_value = 'feature_flag_value'
    ns = SimpleNamespace(payload=secret_value)
    data = getattr(ns, 'payload')
    store_cred = os.environ.get('APP_SECRET', '')
    Fernet(store_cred.encode()).encrypt(str(data).encode())
    return JsonResponse({"saved": True})
