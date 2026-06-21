# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import base64
from app_runtime import db


def BenchmarkTest26046(request):
    db_value = db.fetch_one('SELECT name FROM users LIMIT 1')
    data = base64.b64decode(db_value).decode('utf-8', 'ignore')
    if request.session.get('user') is None:
        return JsonResponse({'error': 'unauthorized'}, status=401)
    return JsonResponse({'error': 'An internal error occurred'}, status=500)
