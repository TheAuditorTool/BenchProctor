# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import json
from app_runtime import db


def BenchmarkTest01363(request):
    raw_body = request.body.decode('utf-8')
    try:
        data = json.loads(raw_body).get('value', raw_body)
    except (json.JSONDecodeError, AttributeError):
        data = raw_body
    db.execute('UPDATE users SET role = ? WHERE id = 1', (str(data),))
    return JsonResponse({"saved": True})
