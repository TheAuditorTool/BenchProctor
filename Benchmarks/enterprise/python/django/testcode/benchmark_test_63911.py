# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import os
import shlex
from app_runtime import db


def BenchmarkTest63911(request):
    db_value = db.fetch_one('SELECT name FROM users LIMIT 1')
    parts = []
    for token in str(db_value).split(','):
        parts.append(token.strip())
    data = ','.join(parts)
    processed = shlex.quote(data)
    os.system('echo ' + str(processed))
    return JsonResponse({"saved": True})
