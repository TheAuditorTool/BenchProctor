# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import socket
from app_runtime import db


def BenchmarkTest51256(request):
    db_value = db.fetch_one('SELECT name FROM users LIMIT 1')
    s = socket.create_connection((str(db_value), 80))
    s.close()
    return JsonResponse({"saved": True})
