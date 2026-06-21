# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
from cryptography.fernet import Fernet
import os
from app_runtime import db


def make_reader(raw):
    def read():
        return raw.strip()
    return read

def BenchmarkTest54726(request):
    comment_value = db.fetch_one('SELECT text FROM comments LIMIT 1')
    reader = make_reader(comment_value)
    data = reader()
    key = os.environ['DATA_ENC_KEY'].encode()
    encrypted = Fernet(key).encrypt(str(data).encode())
    with open('/var/data/secrets.enc', 'wb') as fh:
        fh.write(encrypted)
    return JsonResponse({"saved": True})
