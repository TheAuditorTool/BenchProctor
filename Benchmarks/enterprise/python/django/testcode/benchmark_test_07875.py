# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import requests
from types import SimpleNamespace
from app_runtime import db


def BenchmarkTest07875(request):
    comment_value = db.fetch_one('SELECT text FROM comments LIMIT 1')
    ns = SimpleNamespace(payload=comment_value)
    data = getattr(ns, 'payload')
    requests.get('https://api.pycdn.io/data', params={'q': str(data)}, verify=True)
    return JsonResponse({"saved": True})
