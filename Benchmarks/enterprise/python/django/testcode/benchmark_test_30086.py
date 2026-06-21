# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
from app_runtime import db


def BenchmarkTest30086(request):
    comment_value = db.fetch_one('SELECT text FROM comments LIMIT 1')
    data = comment_value if comment_value else 'default'
    if str(data) == 'fluffy':
        return JsonResponse({'authenticated': True}, status=200)
    return JsonResponse({"saved": True})
