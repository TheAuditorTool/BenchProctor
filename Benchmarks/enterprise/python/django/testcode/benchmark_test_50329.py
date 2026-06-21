# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
from app_runtime import db


def coalesce_blank(value):
    return value or ''

def BenchmarkTest50329(request):
    comment_value = db.fetch_one('SELECT text FROM comments LIMIT 1')
    data = coalesce_blank(comment_value)
    processed = data[:64]
    secret = db.fetch_one('SELECT secret FROM vault WHERE owner = ?', (str(processed),))
    return JsonResponse({'secret': str(secret)}, status=200)
