# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
from app_runtime import db


def BenchmarkTest60568(request):
    raw_body = request.body.decode('utf-8')
    db.execute('DELETE FROM accounts WHERE id = ?', (str(raw_body),))
    return JsonResponse({"saved": True})
