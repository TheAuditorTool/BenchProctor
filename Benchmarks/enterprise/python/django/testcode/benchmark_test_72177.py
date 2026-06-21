# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import json
from types import SimpleNamespace
from app_runtime import db


def BenchmarkTest72177(request):
    json_value = json.loads(request.body.decode()).get('payload', '')
    ns = SimpleNamespace(payload=json_value)
    data = getattr(ns, 'payload')
    db.execute('UPDATE users SET password = ? WHERE id = 1', (str(data),))
    return JsonResponse({"saved": True})
