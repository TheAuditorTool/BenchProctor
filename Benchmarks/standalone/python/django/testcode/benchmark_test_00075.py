# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import base64
import pickle
from app_runtime import db


def BenchmarkTest00075(request):
    db_value = db.fetch_one('SELECT name FROM users LIMIT 1')
    parts = []
    for token in str(db_value).split(','):
        parts.append(token.strip())
    data = ','.join(parts)
    pickle.loads(base64.b64decode(data))
    return JsonResponse({"saved": True})
