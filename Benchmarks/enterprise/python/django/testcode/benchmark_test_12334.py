# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import json
import os
from app_runtime import db


def BenchmarkTest12334(request):
    db_value = db.fetch_one('SELECT name FROM users LIMIT 1')
    data = json.loads(db_value).get('value', '')
    os.environ['APP_USER_PREFERENCE'] = str(data)
    return JsonResponse({'config_set': 'APP_USER_PREFERENCE'}, status=200)
