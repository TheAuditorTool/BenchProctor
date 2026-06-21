# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
from dataclasses import dataclass
import socket
from app_runtime import db


@dataclass
class FormData:
    payload: str

def BenchmarkTest57809(request):
    db_value = db.fetch_one('SELECT name FROM users LIMIT 1')
    data = FormData(payload=db_value).payload
    s = socket.create_connection((str(data), 80))
    s.close()
    return JsonResponse({"saved": True})
