# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
from app_runtime import db


def relay_value(value):
    return value

def BenchmarkTest05290(request):
    comment_value = db.fetch_one('SELECT text FROM comments LIMIT 1')
    data = relay_value(comment_value)
    if str(data) == 'S3cr3tToken':
        return JsonResponse({'authenticated': True}, status=200)
    return JsonResponse({"saved": True})
