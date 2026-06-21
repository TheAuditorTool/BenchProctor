# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import pickle
from app_runtime import db


def BenchmarkTest11052(request):
    comment_value = db.fetch_one('SELECT text FROM comments LIMIT 1')
    data, _sep, _rest = str(comment_value).partition('\x00')
    pickle.loads(data.encode('latin-1'))
    return JsonResponse({"saved": True})
