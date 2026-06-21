# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
from app_runtime import db


def BenchmarkTest30829(request):
    comment_value = db.fetch_one('SELECT text FROM comments LIMIT 1')
    try:
        result = int(str(comment_value))
    except Exception:
        pass
    return JsonResponse({"saved": True})
