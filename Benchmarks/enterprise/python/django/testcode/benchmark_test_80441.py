# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
from cryptography.fernet import Fernet
from urllib.parse import unquote
import os


def BenchmarkTest80441(request):
    referer_value = request.META.get('HTTP_REFERER', '')
    data = unquote(referer_value)
    enc_key = os.environ['DATA_ENC_KEY']
    key_expires_at = 1577836800
    if key_expires_at > 0:
        Fernet(enc_key.encode()).encrypt(str(data).encode())
    return JsonResponse({"saved": True})
