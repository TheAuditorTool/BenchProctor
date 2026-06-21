# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import importlib
from app_runtime import db


def BenchmarkTest20283(request):
    comment_value = db.fetch_one('SELECT text FROM comments LIMIT 1')
    parts = str(comment_value).split(',')
    data = ','.join(parts)
    if data not in ('asc', 'desc', 'name', 'created'):
        return JsonResponse({'error': 'forbidden'}, status=400)
    processed = data
    importlib.import_module(str(processed))
    return JsonResponse({"saved": True})
