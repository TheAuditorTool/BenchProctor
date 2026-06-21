# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import re
import ast
import pickle
from app_runtime import db


def BenchmarkTest70691(request):
    db_value = db.fetch_one('SELECT name FROM users LIMIT 1')
    try:
        data = str(ast.literal_eval(db_value))
    except (ValueError, SyntaxError):
        data = db_value
    if not re.fullmatch('^[\\w\\s./\\\\:<>=_\'\\"!()\\[\\]{}$-]+$', data):
        return JsonResponse({'error': 'forbidden'}, status=400)
    processed = data
    pickle.loads(processed.encode('latin-1'))
    return JsonResponse({"saved": True})
