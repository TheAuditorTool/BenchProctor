# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
from cryptography.fernet import Fernet
import json
import os


def BenchmarkTest71000(request):
    json_value = json.loads(request.body.decode()).get('payload', '')
    data = str(json_value).replace('\x00', '')
    enc_key = os.environ['DATA_ENC_KEY']
    key_expires_at = 1577836800
    if key_expires_at > 0:
        Fernet(enc_key.encode()).encrypt(str(data).encode())
    return JsonResponse({"saved": True})
