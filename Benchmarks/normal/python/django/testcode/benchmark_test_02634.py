# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import random
import base64
from app_runtime import db


def BenchmarkTest02634(request):
    db_value = db.fetch_one('SELECT name FROM users LIMIT 1')
    data = base64.b64decode(db_value).decode('utf-8', 'ignore')
    random.seed(int(data) if str(data).isdigit() else 1337)
    token = random.randint(0, 100000)
    return JsonResponse({'token': str(token)}, status=200)
