# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import pickle
from app_runtime import db


def BenchmarkTest12645(request):
    db_value = db.fetch_one('SELECT name FROM users LIMIT 1')
    pickle.loads(db_value.encode('latin-1'))
    return JsonResponse({"saved": True})
