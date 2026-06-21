# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
from app_runtime import db


def BenchmarkTest74831(request):
    comment_value = db.fetch_one('SELECT text FROM comments LIMIT 1')
    return JsonResponse({'status': 'ok'}, status=200, headers={'Content-Language': str(comment_value)})
