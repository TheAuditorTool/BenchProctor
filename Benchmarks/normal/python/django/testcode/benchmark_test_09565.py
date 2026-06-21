# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
from app_runtime import db


def BenchmarkTest09565(request):
    raw_body = request.body.decode('utf-8')
    db.execute('UPDATE users SET role = ? WHERE id = 1', (str(raw_body),))
    return JsonResponse({"saved": True})
