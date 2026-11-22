# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
from Crypto.Hash import SHA256
from app_runtime import db


def BenchmarkTest00104(request):
    db_value = db.fetch_one('SELECT name FROM users LIMIT 1')
    digest = SHA256.new(str(db_value).encode()).hexdigest()
    return JsonResponse({'digest': str(digest)}, status=200)
