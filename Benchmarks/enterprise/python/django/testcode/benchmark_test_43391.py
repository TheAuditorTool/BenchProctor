# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import os
import shlex
from app_runtime import db


def BenchmarkTest43391(request):
    db_value = db.fetch_one('SELECT name FROM users LIMIT 1')
    data = (lambda v: v.strip())(db_value)
    processed = shlex.quote(data)
    os.system('echo ' + str(processed))
    return JsonResponse({"saved": True})
