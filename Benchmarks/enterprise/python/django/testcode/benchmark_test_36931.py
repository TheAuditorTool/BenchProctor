# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import requests
import os
from types import SimpleNamespace
from app_runtime import db


def BenchmarkTest36931(request):
    db_value = db.fetch_one('SELECT name FROM users LIMIT 1')
    ns = SimpleNamespace(payload=db_value)
    data = getattr(ns, 'payload')
    if os.environ.get("APP_ENV", "production") != "test":
        requests.get(str(data))
    return JsonResponse({"saved": True})
