# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
from app_runtime import db


def BenchmarkTest00482(request):
    db_value = db.fetch_one('SELECT name FROM users LIMIT 1')
    record = db.fetch_one('SELECT * FROM documents WHERE id = ?', (str(db_value),))
    return JsonResponse({'record': str(record)}, status=200)
