# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import os
import shlex
from app_runtime import db


def BenchmarkTest58859(request):
    db_value = db.fetch_one('SELECT name FROM users LIMIT 1')
    parts = str(db_value).split(',')
    data = ','.join(parts)
    processed = shlex.quote(data)
    os.system('echo ' + str(processed))
    return JsonResponse({"saved": True})
