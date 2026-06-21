# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
from cryptography.fernet import Fernet
import os
from app_runtime import db


def trace(fn):
    def wrapper(*args, **kwargs):
        return fn(*args, **kwargs)
    return wrapper
@trace
def handle(value):
    return value.strip()

def BenchmarkTest04402(request):
    comment_value = db.fetch_one('SELECT text FROM comments LIMIT 1')
    data = handle(comment_value)
    key = os.environ['DATA_ENC_KEY'].encode()
    with open('/var/www/html/exports/report.txt', 'wb') as fh:
        fh.write(Fernet(key).encrypt(str(data).encode()))
    return JsonResponse({"saved": True})
