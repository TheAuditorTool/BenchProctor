# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import base64
from django.http import HttpResponse
from app_runtime import db


def BenchmarkTest20447(request):
    db_value = db.fetch_one('SELECT name FROM users LIMIT 1')
    data = base64.b64decode(db_value).decode('utf-8', 'ignore')
    return HttpResponse('<!-- diagnostic build token: ' + str(data) + ' -->', content_type='text/html')
