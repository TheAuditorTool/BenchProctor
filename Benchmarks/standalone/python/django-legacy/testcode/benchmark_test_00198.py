# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
from Crypto.Hash import SHA256
from app_runtime import db


def BenchmarkTest00198(request):
    db_value = db.fetch_one('SELECT name FROM users LIMIT 1')
    def normalize(value):
        return value.strip()
    data = normalize(db_value)
    digest = SHA256.new(str(data).encode()).hexdigest()
    return JsonResponse({'digest': str(digest)}, status=200)
