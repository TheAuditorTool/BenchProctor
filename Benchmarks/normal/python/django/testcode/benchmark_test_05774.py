# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import tempfile
from app_runtime import db


def BenchmarkTest05774(request):
    comment_value = db.fetch_one('SELECT text FROM comments LIMIT 1')
    collected = None
    def on_input(value):
        nonlocal collected
        collected = value
    on_input(comment_value)
    data = collected
    path = tempfile.mktemp()
    with open(path, 'w') as fh:
        fh.write(str(data))
    return JsonResponse({"saved": True})
