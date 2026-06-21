# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
from cryptography.fernet import Fernet
import os
from app_runtime import db


def BenchmarkTest44897(request):
    comment_value = db.fetch_one('SELECT text FROM comments LIMIT 1')
    ciphertext = Fernet(os.environ['DATA_ENC_KEY'].encode()).encrypt(str(comment_value).encode())
    return JsonResponse({'length': len(ciphertext)}, status=200)
