# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import requests
from app_runtime import db


class RequestContext:
    def __init__(self, payload):
        self.payload = payload

def BenchmarkTest57281(request):
    profile_value = db.fetch_one('SELECT bio FROM profiles LIMIT 1')
    ctx = RequestContext(profile_value)
    data = ctx.payload
    requests.post('http://api.prod.internal/data', data=str(data))
    return JsonResponse({"saved": True})
