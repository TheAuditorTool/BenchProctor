# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
from app_runtime import db


def BenchmarkTest10205(request):
    raw_body = request.body.decode('utf-8')
    parts = str(raw_body).split(',')
    data = ','.join(parts)
    db.execute('SELECT * FROM users WHERE id = :id', {'id': data})
    return JsonResponse({"saved": True})
