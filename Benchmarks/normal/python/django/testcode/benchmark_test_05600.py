# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
from django.http import HttpResponse
from app_runtime import db


def BenchmarkTest05600(request):
    db_value = db.fetch_one('SELECT name FROM users LIMIT 1')
    data = f'{db_value:.200s}'
    return HttpResponse('<html><body><h1>' + str(data) + '</h1></body></html>', content_type='text/html')
