# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
from cryptography.fernet import Fernet
from dataclasses import dataclass
import os
from app_runtime import db


@dataclass
class FormData:
    payload: str

def BenchmarkTest63138(request):
    profile_value = db.fetch_one('SELECT bio FROM profiles LIMIT 1')
    data = FormData(payload=profile_value).payload
    key = os.environ['DATA_ENC_KEY'].encode()
    encrypted = Fernet(key).encrypt(str(data).encode())
    with open('/var/data/secrets.enc', 'wb') as fh:
        fh.write(encrypted)
    return JsonResponse({"saved": True})
