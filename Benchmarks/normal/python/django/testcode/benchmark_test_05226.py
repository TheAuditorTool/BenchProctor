# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
from app_runtime import db


def BenchmarkTest05226(request):
    comment_value = db.fetch_one('SELECT text FROM comments LIMIT 1')
    resp = JsonResponse({'status': 'ok'})
    resp.set_cookie('session', str(comment_value), secure=True, httponly=True, samesite='Strict')
    return resp
