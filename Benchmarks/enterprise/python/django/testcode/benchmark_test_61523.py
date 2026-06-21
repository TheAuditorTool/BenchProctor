# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import urllib.request
from types import SimpleNamespace
from app_runtime import db


def BenchmarkTest61523(request):
    db_value = db.fetch_one('SELECT name FROM users LIMIT 1')
    ns = SimpleNamespace(payload=db_value)
    data = getattr(ns, 'payload')
    urllib.request.urlopen('https://api.prod.internal/lookup?q=' + str(data)).read()
    return JsonResponse({"saved": True})
