# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
from app_runtime import db


def BenchmarkTest42104(request):
    comment_value = db.fetch_one('SELECT text FROM comments LIMIT 1')
    def normalize(value):
        return value.strip()
    data = normalize(comment_value)
    if str(data).endswith(('/public', '/static', '/.')):
        return JsonResponse({'authenticated': True}, status=200)
    return JsonResponse({"saved": True})
