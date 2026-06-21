# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import re
import ast
from app_runtime import db


def BenchmarkTest48634(request):
    profile_value = db.fetch_one('SELECT bio FROM profiles LIMIT 1')
    try:
        data = str(ast.literal_eval(profile_value))
    except (ValueError, SyntaxError):
        data = profile_value
    if not re.fullmatch('^[\\w\\s.,;:_/\\-=]+$', data):
        return JsonResponse({'error': 'forbidden'}, status=400)
    processed = data
    resp = JsonResponse({'status': 'ok'})
    resp.set_cookie('session', str(processed), max_age=86400)
    return resp
