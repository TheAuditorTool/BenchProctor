# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import os
from app_runtime import db


class RequestContext:
    def __init__(self, payload):
        self.payload = payload

def BenchmarkTest79000(request):
    comment_value = db.fetch_one('SELECT text FROM comments LIMIT 1')
    ctx = RequestContext(comment_value)
    data = ctx.payload
    allowed = {'config.json', 'index.html', 'readme.md'}
    if data not in allowed:
        return JsonResponse({'error': 'forbidden'}, status=403)
    checked_path = '/var/app/data/' + data
    with open(checked_path, 'wb') as fh:
        fh.write(b'data')
    return JsonResponse({"saved": True})
