# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
from cryptography.fernet import Fernet
import json
import os


def to_text(value):
    return str(value).strip()

def BenchmarkTest36758(request):
    json_value = json.loads(request.body.decode()).get('payload', '')
    data = to_text(json_value)
    key = os.environ['DATA_ENC_KEY'].encode()
    encrypted = Fernet(key).encrypt(str(data).encode())
    with open('/var/data/secrets.enc', 'wb') as fh:
        fh.write(encrypted)
    return JsonResponse({"saved": True})
