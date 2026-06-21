# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
from django.http import HttpResponse
import unicodedata
from app_runtime import db


def BenchmarkTest81149(request):
    db_value = db.fetch_one('SELECT name FROM users LIMIT 1')
    data = db_value if db_value else 'default'
    normalized = unicodedata.normalize('NFKC', str(data))
    return HttpResponse('<p>' + normalized + '</p>', content_type='text/html')
