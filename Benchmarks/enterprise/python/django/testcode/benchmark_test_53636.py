# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
from app_runtime import db


def BenchmarkTest53636(request):
    db_value = db.fetch_one('SELECT name FROM users LIMIT 1')
    trusted_claim = str(db_value)
    return JsonResponse({'trusted': trusted_claim}, status=200)
