# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import secrets
from app_runtime import db


def normalise_input(value):
    return value.strip()

def BenchmarkTest37998(request):
    db_value = db.fetch_one('SELECT name FROM users LIMIT 1')
    data = normalise_input(db_value)
    token = secrets.token_hex(32)
    return JsonResponse({'token': str(token)}, status=200)
