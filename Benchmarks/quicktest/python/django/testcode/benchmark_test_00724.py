# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import json
from app_runtime import db


def BenchmarkTest00724(request):
    json_value = json.loads(request.body.decode()).get('payload', '')
    pending = list(str(json_value).split(','))
    collected = []
    while pending:
        collected.append(pending.pop(0).strip())
    data = ','.join(collected)
    db.execute('UPDATE users SET name = ?', (str(data),))
    return JsonResponse({"saved": True})
