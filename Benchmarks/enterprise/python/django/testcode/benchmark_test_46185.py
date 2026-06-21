# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import json
import socket
from app_runtime import db


def BenchmarkTest46185(request):
    db_value = db.fetch_one('SELECT name FROM users LIMIT 1')
    data = json.loads(db_value).get('value', '')
    s = socket.create_connection((str(data), 80))
    s.close()
    return JsonResponse({"saved": True})
