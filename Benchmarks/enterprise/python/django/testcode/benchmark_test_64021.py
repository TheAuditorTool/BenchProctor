# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
from app_runtime import db


def BenchmarkTest64021(request):
    comment_value = db.fetch_one('SELECT text FROM comments LIMIT 1')
    data = (lambda v: v.strip())(comment_value)
    try:
        result = int(str(data))
    except Exception:
        pass
    return JsonResponse({"saved": True})
