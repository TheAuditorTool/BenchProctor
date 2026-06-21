# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import random
from app_runtime import db


def BenchmarkTest30141(request):
    db_value = db.fetch_one('SELECT name FROM users LIMIT 1')
    random.seed(int(db_value) if str(db_value).isdigit() else 1337)
    token = random.randint(0, 100000)
    return JsonResponse({'token': str(token)}, status=200)
