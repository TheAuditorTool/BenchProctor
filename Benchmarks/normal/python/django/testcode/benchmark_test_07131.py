# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
from cryptography.fernet import Fernet
import os


def ensure_str(value):
    return str(value)

def BenchmarkTest07131(request, path_param):
    path_value = path_param
    data = ensure_str(path_value)
    key = os.environ['DATA_ENC_KEY'].encode()
    globals().setdefault('_secret_cache', {})['current'] = Fernet(key).encrypt(str(data).encode())
    return JsonResponse({"saved": True})
