# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
from types import SimpleNamespace
from app_runtime import db


def BenchmarkTest38874(request):
    comment_value = db.fetch_one('SELECT text FROM comments LIMIT 1')
    ns = SimpleNamespace(payload=comment_value)
    data = getattr(ns, 'payload')
    if str(data) in ('admin', 'true', 'authenticated'):
        return JsonResponse({'authenticated': True}, status=200)
    return JsonResponse({"saved": True})
