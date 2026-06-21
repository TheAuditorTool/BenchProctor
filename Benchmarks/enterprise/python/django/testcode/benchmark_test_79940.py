# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import yaml
import json
from app_runtime import db


class RequestContext:
    def __init__(self, payload):
        self.payload = payload

def BenchmarkTest79940(request):
    comment_value = db.fetch_one('SELECT text FROM comments LIMIT 1')
    ctx = RequestContext(comment_value)
    data = ctx.payload
    yaml.safe_load(data)
    return JsonResponse({"saved": True})
