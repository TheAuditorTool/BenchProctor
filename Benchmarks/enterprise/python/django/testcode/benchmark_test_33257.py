# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import tempfile
from app_runtime import db


def BenchmarkTest33257(request):
    comment_value = db.fetch_one('SELECT text FROM comments LIMIT 1')
    if comment_value:
        data = comment_value
    else:
        data = ''
    path = tempfile.mktemp()
    with open(path, 'w') as fh:
        fh.write(str(data))
    return JsonResponse({"saved": True})
