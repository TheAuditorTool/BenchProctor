# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import re
import ast
from app_runtime import db


def BenchmarkTest67104(request):
    secret_value = 'sk-proj-EXAMPLEdummy0123456789abcdefABCD'
    try:
        data = str(ast.literal_eval(secret_value))
    except (ValueError, SyntaxError):
        data = secret_value
    if not re.fullmatch('^[\\w\\s.,;:_/\\-=]+$', data):
        return JsonResponse({'error': 'forbidden'}, status=400)
    processed = data
    db.connect(host='localhost', user='app', password=processed)
    return JsonResponse({"saved": True})
