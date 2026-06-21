# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import base64
from django.shortcuts import redirect
import urllib.parse
from app_runtime import db


def BenchmarkTest33367(request):
    db_value = db.fetch_one('SELECT name FROM users LIMIT 1')
    data = base64.b64decode(db_value).decode('utf-8', 'ignore')
    if data not in ('asc', 'desc', 'name', 'created'):
        return JsonResponse({'error': 'forbidden'}, status=400)
    processed = data
    target = '/dashboard?hidden_field=' + urllib.parse.quote(str(processed))
    return redirect(target)
