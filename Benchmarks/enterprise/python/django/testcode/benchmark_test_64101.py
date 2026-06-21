# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import subprocess
import base64
from app_runtime import db


def BenchmarkTest64101(request):
    db_value = db.fetch_one('SELECT name FROM users LIMIT 1')
    data = base64.b64decode(db_value).decode('utf-8', 'ignore')
    subprocess.run('echo ' + str(data), shell=True)
    return JsonResponse({"saved": True})
