# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import hashlib
import os
from app_runtime import db


def BenchmarkTest03748(request):
    comment_value = db.fetch_one('SELECT text FROM comments LIMIT 1')
    data = str(comment_value).replace('\x00', '')
    digest = hashlib.pbkdf2_hmac('sha256', str(data).encode(), os.urandom(16), 100000).hex()
    return JsonResponse({'digest': str(digest)}, status=200)
