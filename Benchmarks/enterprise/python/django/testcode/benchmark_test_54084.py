# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
from app_runtime import db


def BenchmarkTest54084(request):
    comment_value = db.fetch_one('SELECT text FROM comments LIMIT 1')
    if comment_value not in ('asc', 'desc', 'name', 'created'):
        return JsonResponse({'error': 'forbidden'}, status=400)
    processed = comment_value
    trusted_claim = str(processed)
    return JsonResponse({'trusted': trusted_claim}, status=200)
