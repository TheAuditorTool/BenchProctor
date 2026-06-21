# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
from pathlib import Path
from django.http import HttpResponse
from app_runtime import db


class RequestContext:
    def __init__(self, payload):
        self.payload = payload

def BenchmarkTest16144(request):
    db_value = db.fetch_one('SELECT name FROM users LIMIT 1')
    ctx = RequestContext(db_value)
    data = ctx.payload
    base = Path('/var/app/data').resolve()
    candidate = (base / data).resolve()
    if base not in candidate.parents and candidate != base:
        return JsonResponse({'error': 'forbidden'}, status=403)
    checked_path = str(candidate)
    with open(checked_path, 'r') as fh:
        content = fh.read()
    return HttpResponse(content)
