# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
from app_runtime import db


def BenchmarkTest00168(request):
    db_value = db.fetch_one('SELECT name FROM users LIMIT 1')
    data = '%s' % (db_value,)
    _coerced = 'true' if str(data).lower() in ('true', '1', 'yes', 'on') else 'false'
    processed = _coerced
    code = compile(str(processed), '<rule>', 'exec')
    exec(code)
    return JsonResponse({"saved": True})
