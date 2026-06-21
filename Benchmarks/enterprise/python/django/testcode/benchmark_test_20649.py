# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import hashlib
import base64
from app_runtime import db


def BenchmarkTest20649(request):
    db_value = db.fetch_one('SELECT name FROM users LIMIT 1')
    data = base64.b64decode(db_value).decode('utf-8', 'ignore')
    digest = str(data).encode().hex()
    return JsonResponse({'digest': str(digest)}, status=200)
