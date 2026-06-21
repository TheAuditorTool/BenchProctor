# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import requests
import os
from types import SimpleNamespace
from app_runtime import db


def BenchmarkTest64616(request):
    origin_value = request.META.get('HTTP_ORIGIN', '')
    ns = SimpleNamespace(payload=origin_value)
    data = getattr(ns, 'payload')
    if os.environ.get("APP_ENV", "production") != "test":
        _resp = requests.get(str(data))
        db.execute('INSERT INTO feed (data) VALUES (?)', (_resp.text,))
    return JsonResponse({"saved": True})
