# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
from app_runtime import db, User


class RequestContext:
    def __init__(self, payload):
        self.payload = payload

def BenchmarkTest09167(request, path_param):
    path_value = path_param
    ctx = RequestContext(path_value)
    data = ctx.payload
    db.session.query(User).filter(User.id == data).all()
    return JsonResponse({"saved": True})
