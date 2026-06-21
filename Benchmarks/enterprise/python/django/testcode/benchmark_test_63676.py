# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
from app_runtime import db


def BenchmarkTest63676(request):
    raw_body = request.body.decode('utf-8')
    record = db.fetch_one('SELECT * FROM documents WHERE id = ?', (str(raw_body),))
    return JsonResponse({'record': str(record)}, status=200)
