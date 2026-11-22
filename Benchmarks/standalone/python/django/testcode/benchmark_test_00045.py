# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import random
import json
from app_runtime import db


def BenchmarkTest00045(request):
    db_value = db.fetch_one('SELECT name FROM users LIMIT 1')
    data = json.loads(db_value).get('value', '')
    token = random.randbytes(16).hex()
    db.execute('INSERT INTO reset_tokens (account, token) VALUES (?, ?)', (str(data), token))
    return JsonResponse({'token': str(token)}, status=200)
