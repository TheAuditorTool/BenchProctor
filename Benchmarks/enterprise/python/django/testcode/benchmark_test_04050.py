# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import socket
from app_runtime import db


def BenchmarkTest04050(request):
    db_value = db.fetch_one('SELECT name FROM users LIMIT 1')
    parts = str(db_value).split(',')
    data = ','.join(parts)
    s = socket.create_connection((str(data), 80))
    s.close()
    return JsonResponse({"saved": True})
