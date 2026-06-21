# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
from app_runtime import db


def relay_value(value):
    return value

def BenchmarkTest51196(request):
    comment_value = db.fetch_one('SELECT text FROM comments LIMIT 1')
    data = relay_value(comment_value)
    processed = data[:64]
    return JsonResponse({'status': 'ok'}, status=200, headers={'X-Echo': str(processed)})
