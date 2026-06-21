# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import json
from app_runtime import db


def BenchmarkTest18916(request):
    raw_body = request.body.decode('utf-8')
    data = json.loads(raw_body).get('value', '')
    db.execute('SELECT * FROM users WHERE id = ?', (data,))
    return JsonResponse({"saved": True})
