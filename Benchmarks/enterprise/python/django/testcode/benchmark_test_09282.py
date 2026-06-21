# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import tempfile
import os
from app_runtime import db


def BenchmarkTest09282(request):
    comment_value = db.fetch_one('SELECT text FROM comments LIMIT 1')
    data = f'{comment_value}'
    fd, path = tempfile.mkstemp(prefix='upload_', dir='/var/app/tmp')
    with os.fdopen(fd, 'w') as fh:
        fh.write(str(data))
    return JsonResponse({"saved": True})
