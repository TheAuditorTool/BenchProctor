# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import subprocess
from types import SimpleNamespace
from app_runtime import db


def BenchmarkTest18312(request):
    db_value = db.fetch_one('SELECT name FROM users LIMIT 1')
    ns = SimpleNamespace(payload=db_value)
    data = getattr(ns, 'payload')
    processed = data[:64]
    subprocess.run('echo ' + str(processed), shell=True)
    return JsonResponse({"saved": True})
