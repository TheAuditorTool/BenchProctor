# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
from app_runtime import db


def make_reader(raw):
    def read():
        return raw.strip()
    return read

def BenchmarkTest50219(request):
    db_value = db.fetch_one('SELECT name FROM users LIMIT 1')
    reader = make_reader(db_value)
    data = reader()
    size = min(int(data) if str(data).isdigit() else 0, 1024)
    data = bytearray(size)
    return JsonResponse({"saved": True})
