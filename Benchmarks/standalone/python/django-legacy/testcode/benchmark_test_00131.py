# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
from app_runtime import db


def BenchmarkTest00131(request):
    raw_body = request.body.decode('utf-8')
    data, _sep, _rest = str(raw_body).partition('\x00')
    result = db.fetch_one('SELECT name FROM users WHERE id = ?', (str(data),))
    value = result['name']
    return JsonResponse({'name': str(value)}, status=200)
