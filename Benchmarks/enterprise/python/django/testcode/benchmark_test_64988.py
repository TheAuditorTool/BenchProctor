# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
from app_runtime import db


def BenchmarkTest64988(request):
    comment_value = db.fetch_one('SELECT text FROM comments LIMIT 1')
    arr = [10, 20, 30, 40, 50]
    idx = int(str(comment_value))
    return JsonResponse({'lookup': arr[idx]}, status=200)
