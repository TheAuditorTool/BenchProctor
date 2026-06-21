# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
from app_runtime import db


def BenchmarkTest05749(request):
    comment_value = db.fetch_one('SELECT text FROM comments LIMIT 1')
    parts = str(comment_value).split(',')
    data = ','.join(parts)
    resp = JsonResponse({'status': 'ok'})
    resp.set_cookie('session', str(data))
    return resp
