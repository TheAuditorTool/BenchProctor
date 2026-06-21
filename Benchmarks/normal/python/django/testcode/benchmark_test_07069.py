# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import json
from django.http import HttpResponse
from app_runtime import db


def BenchmarkTest07069(request):
    db_value = db.fetch_one('SELECT name FROM users LIMIT 1')
    data = json.loads(db_value).get('value', '')
    if data not in ('asc', 'desc', 'name', 'created'):
        return JsonResponse({'error': 'forbidden'}, status=400)
    processed = data
    return HttpResponse(str(processed), content_type='text/html')
