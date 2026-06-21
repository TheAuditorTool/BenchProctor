# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import defusedxml.ElementTree
from app_runtime import db


class RequestContext:
    def __init__(self, payload):
        self.payload = payload

def BenchmarkTest59984(request):
    db_value = db.fetch_one('SELECT name FROM users LIMIT 1')
    ctx = RequestContext(db_value)
    data = ctx.payload
    defusedxml.ElementTree.fromstring(str(data))
    return JsonResponse({"saved": True})
