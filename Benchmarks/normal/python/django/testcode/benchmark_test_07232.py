# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import os
import tempfile
from app_runtime import db


request_state: dict[str, str] = {}

def BenchmarkTest07232(request):
    comment_value = db.fetch_one('SELECT text FROM comments LIMIT 1')
    request_state['last_input'] = comment_value
    data = request_state['last_input']
    fd, path = tempfile.mkstemp(prefix='upload_', dir='/var/app/tmp')
    with os.fdopen(fd, 'w') as fh:
        fh.write(str(data))
    os.chmod(path, 0o777)
    return JsonResponse({"saved": True})
