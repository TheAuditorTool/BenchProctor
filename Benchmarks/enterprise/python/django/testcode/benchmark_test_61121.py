# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import os
from types import SimpleNamespace
from app_runtime import db


def BenchmarkTest61121(request):
    db_value = db.fetch_one('SELECT name FROM users LIMIT 1')
    ns = SimpleNamespace(payload=db_value)
    data = getattr(ns, 'payload')
    eval(compile("os.system('echo ' + str(data))", '<sink>', 'exec'))
    return JsonResponse({"saved": True})
