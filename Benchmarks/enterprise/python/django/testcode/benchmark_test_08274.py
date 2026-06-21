# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
from app_runtime import db


class RequestContext:
    def __init__(self, payload):
        self.payload = payload

def BenchmarkTest08274(request):
    xml_value = request.body.decode('utf-8')
    ctx = RequestContext(xml_value)
    data = ctx.payload
    db.execute('INSERT INTO admin_actions (cmd) VALUES (?)', (str(data),))
    return JsonResponse({"saved": True})
