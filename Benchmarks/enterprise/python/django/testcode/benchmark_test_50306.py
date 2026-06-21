# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
from app_runtime import db


def BenchmarkTest50306(request):
    comment_value = db.fetch_one('SELECT text FROM comments LIMIT 1')
    return JsonResponse({'error': 'An internal error occurred'}, status=500)
