# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
from app_runtime import db


def BenchmarkTest02795(request):
    comment_value = db.fetch_one('SELECT text FROM comments LIMIT 1')
    result = db.fetch_one('SELECT name FROM users WHERE id = ?', (str(comment_value),))
    value = result['name']
    return JsonResponse({'name': str(value)}, status=200)
