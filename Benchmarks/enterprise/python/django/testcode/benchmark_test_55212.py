# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import hashlib
import os
from app_runtime import db


def BenchmarkTest55212(request):
    db_value = db.fetch_one('SELECT name FROM users LIMIT 1')
    digest = hashlib.pbkdf2_hmac('sha256', str(db_value).encode(), os.urandom(16), 100000).hex()
    return JsonResponse({'digest': str(digest)}, status=200)
