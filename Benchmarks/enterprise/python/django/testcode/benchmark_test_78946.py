# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import secrets
from types import SimpleNamespace
from app_runtime import db


def BenchmarkTest78946(request):
    db_value = db.fetch_one('SELECT name FROM users LIMIT 1')
    ns = SimpleNamespace(payload=db_value)
    data = getattr(ns, 'payload')
    token = secrets.token_hex(32)
    return JsonResponse({'token': str(token)}, status=200)
