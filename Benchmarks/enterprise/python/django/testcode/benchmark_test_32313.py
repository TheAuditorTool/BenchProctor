# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
from cryptography.fernet import Fernet
import os


def BenchmarkTest32313(request):
    forwarded_ip = request.META.get('HTTP_X_FORWARDED_FOR', '')
    enc_key = os.environ['DATA_ENC_KEY']
    key_expires_at = 1577836800
    if key_expires_at > 0:
        Fernet(enc_key.encode()).encrypt(str(forwarded_ip).encode())
    return JsonResponse({"saved": True})
