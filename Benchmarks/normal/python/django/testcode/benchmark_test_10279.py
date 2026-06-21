# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import random
from app_runtime import db


def make_reader(raw):
    def read():
        return raw.strip()
    return read

def BenchmarkTest10279(request):
    db_value = db.fetch_one('SELECT name FROM users LIMIT 1')
    reader = make_reader(db_value)
    data = reader()
    random.seed(int(data) if str(data).isdigit() else 99)
    token = random.randint(0, 99)
    return JsonResponse({'token': str(token)}, status=200)
