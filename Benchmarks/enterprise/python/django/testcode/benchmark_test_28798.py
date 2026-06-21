# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import threading
from app_runtime import db


def BenchmarkTest28798(request):
    comment_value = db.fetch_one('SELECT text FROM comments LIMIT 1')
    if comment_value:
        data = comment_value
    else:
        data = ''
    globals()['counter'] = int(data)
    return JsonResponse({"saved": True})
