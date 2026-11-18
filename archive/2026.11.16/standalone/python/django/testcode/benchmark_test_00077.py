# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import hashlib
from app_runtime import db


def BenchmarkTest00077(request):
    db_value = db.fetch_one('SELECT name FROM users LIMIT 1')
    data = db_value if db_value else 'default'
    digest = hashlib.sha256(str(data).encode()).hexdigest()
    return JsonResponse({'digest': str(digest)}, status=200)
