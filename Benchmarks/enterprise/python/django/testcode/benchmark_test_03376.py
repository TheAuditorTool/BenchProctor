# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
from app_runtime import db


def BenchmarkTest03376(request):
    comment_value = db.fetch_one('SELECT text FROM comments LIMIT 1')
    db.execute('SELECT * FROM users WHERE id = ?', (comment_value,))
    return JsonResponse({"saved": True})
