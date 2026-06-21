# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import json
from app_runtime import db


def BenchmarkTest03823(request):
    json_value = json.loads(request.body.decode()).get('payload', '')
    if json_value:
        data = json_value
    else:
        data = ''
    db.execute('SELECT * FROM users WHERE id = :id', {'id': data})
    return JsonResponse({"saved": True})
