# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
from app_runtime import db


def BenchmarkTest80167(request):
    comment_value = db.fetch_one('SELECT text FROM comments LIMIT 1')
    data, _sep, _rest = str(comment_value).partition('\x00')
    try:
        result = int(str(data))
    except ValueError as e:
        return JsonResponse({'error': str(e)}, status=400)
    return JsonResponse({"saved": True})
