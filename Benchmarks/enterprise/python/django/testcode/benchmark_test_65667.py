# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
from app_runtime import db


class RequestContext:
    def __init__(self, payload):
        self.payload = payload

def BenchmarkTest65667(request):
    user_id = request.GET.get('id', '')
    ctx = RequestContext(user_id)
    data = ctx.payload
    db.execute('UPDATE users SET role = ? WHERE name = ?', ('admin', str(data)))
    return JsonResponse({"saved": True})
