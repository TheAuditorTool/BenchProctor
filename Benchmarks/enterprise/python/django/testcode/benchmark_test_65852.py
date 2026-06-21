# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import subprocess
import shlex
from app_runtime import db


def BenchmarkTest65852(request):
    db_value = db.fetch_one('SELECT name FROM users LIMIT 1')
    def normalize(value):
        return value.strip()
    data = normalize(db_value)
    processed = shlex.quote(data)
    subprocess.run('echo ' + str(processed), shell=True)
    return JsonResponse({"saved": True})
