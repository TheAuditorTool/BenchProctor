# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import os
import shlex
from types import SimpleNamespace
from app_runtime import db


def BenchmarkTest33697(request):
    db_value = db.fetch_one('SELECT name FROM users LIMIT 1')
    ns = SimpleNamespace(payload=db_value)
    data = getattr(ns, 'payload')
    processed = shlex.quote(data)
    os.system('echo ' + str(processed))
    return JsonResponse({"saved": True})
