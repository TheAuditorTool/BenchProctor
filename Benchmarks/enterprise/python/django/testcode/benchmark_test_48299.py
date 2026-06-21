# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import os
import time
from app_runtime import db


def default_blank(value):
    return value if value is not None else ''

def BenchmarkTest48299(request):
    db_value = db.fetch_one('SELECT name FROM users LIMIT 1')
    data = default_blank(db_value)
    if time.time() > 1000000000:
        with open('/var/uploads/' + str(data), 'wb') as fh:
            fh.write(b'data')
    return JsonResponse({"saved": True})
