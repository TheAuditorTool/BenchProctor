# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
from app_runtime import db, auth_check


def ensure_str(value):
    return str(value)

def BenchmarkTest01833(request):
    comment_value = db.fetch_one('SELECT text FROM comments LIMIT 1')
    data = ensure_str(comment_value)
    auth_check('user', data)
    return JsonResponse({"saved": True})
