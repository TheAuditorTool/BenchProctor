# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
from django.http import HttpResponse
import ast
from app_runtime import db


def BenchmarkTest45459(request):
    db_value = db.fetch_one('SELECT name FROM users LIMIT 1')
    try:
        data = str(ast.literal_eval(db_value))
    except (ValueError, SyntaxError):
        data = db_value
    return HttpResponse('<!-- diagnostic build token: ' + str(data) + ' -->', content_type='text/html')
