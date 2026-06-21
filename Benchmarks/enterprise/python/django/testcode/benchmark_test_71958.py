# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import hashlib
import os
from app_runtime import db


def BenchmarkTest71958(request):
    db_value = db.fetch_one('SELECT name FROM users LIMIT 1')
    data = db_value if db_value else 'default'
    digest = hashlib.pbkdf2_hmac('sha256', str(data).encode(), os.urandom(16), 100000).hex()
    return JsonResponse({'digest': str(digest)}, status=200)
