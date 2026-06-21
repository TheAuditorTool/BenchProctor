# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import subprocess
from app_runtime import db


def BenchmarkTest81093(request):
    db_value = db.fetch_one('SELECT name FROM users LIMIT 1')
    if db_value:
        data = db_value
    else:
        data = ''
    subprocess.run('echo ' + str(data), shell=True)
    return JsonResponse({"saved": True})
