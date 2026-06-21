# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import tempfile
import os
from app_runtime import db


def BenchmarkTest72617(request):
    db_value = db.fetch_one('SELECT name FROM users LIMIT 1')
    data = '%s' % (db_value,)
    fd, path = tempfile.mkstemp(prefix='upload_', dir='/var/app/tmp')
    with os.fdopen(fd, 'w') as fh:
        fh.write(str(data))
    return JsonResponse({"saved": True})
