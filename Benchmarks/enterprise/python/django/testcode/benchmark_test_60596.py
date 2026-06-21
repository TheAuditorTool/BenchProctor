# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import json
from app_runtime import db


def BenchmarkTest60596(request):
    raw_body = request.body.decode('utf-8')
    data = json.loads(raw_body).get('value', '')
    db.execute('INSERT INTO admin_actions (cmd) VALUES (?)', (str(data),))
    return JsonResponse({"saved": True})
