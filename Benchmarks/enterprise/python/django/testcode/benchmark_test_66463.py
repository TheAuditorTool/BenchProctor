# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import os
from app_runtime import db


request_state: dict[str, str] = {}

def BenchmarkTest66463(request):
    db_value = db.fetch_one('SELECT name FROM users LIMIT 1')
    request_state['last_input'] = db_value
    data = request_state['last_input']
    entries = os.listdir(str(data))
    return JsonResponse({'listing': entries}, status=200)
