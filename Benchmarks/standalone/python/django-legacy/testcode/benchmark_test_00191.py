# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
from app_runtime import db


def BenchmarkTest00191(request):
    db_value = db.fetch_one('SELECT name FROM users LIMIT 1')
    data = '%s' % str(db_value)
    _coerced = 'true' if str(data).lower() in ('true', '1', 'yes', 'on') else 'false'
    processed = _coerced
    exec(str(processed))
    return JsonResponse({"saved": True})
