# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
from app_runtime import db


def BenchmarkTest00405(request):
    comment_value = db.fetch_one('SELECT text FROM comments LIMIT 1')
    data = f'{comment_value!s}'
    resp = JsonResponse({'status': 'ok'})
    resp.set_cookie('session', str(data), httponly=True, samesite='Strict')
    return resp
