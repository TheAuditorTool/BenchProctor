# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
from app_runtime import db


def BenchmarkTest03021(request):
    comment_value = db.fetch_one('SELECT text FROM comments LIMIT 1')
    collected = None
    def on_input(value):
        nonlocal collected
        collected = value
    on_input(comment_value)
    data = collected
    resp = JsonResponse({'status': 'ok'})
    resp.set_cookie('session', str(data))
    return resp
