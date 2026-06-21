# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import pickle
from app_runtime import db


class RequestContext:
    def __init__(self, payload):
        self.payload = payload

def BenchmarkTest73705(request):
    comment_value = db.fetch_one('SELECT text FROM comments LIMIT 1')
    ctx = RequestContext(comment_value)
    data = ctx.payload
    processed = data[:64]
    pickle.loads(processed.encode('latin-1'))
    return JsonResponse({"saved": True})
