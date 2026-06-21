# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
from app_runtime import db


def BenchmarkTest39536(request):
    comment_value = db.fetch_one('SELECT text FROM comments LIMIT 1')
    parts = str(comment_value).split(',')
    data = ','.join(parts)
    return JsonResponse({'status': 'ok'}, status=200, headers={'Access-Control-Allow-Origin': str(data)})
