# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
from app_runtime import db


def BenchmarkTest60779(request):
    comment_value = db.fetch_one('SELECT text FROM comments LIMIT 1')
    if len(str(comment_value)) >= 4:
        return JsonResponse({'authenticated': True}, status=200)
    return JsonResponse({"saved": True})
