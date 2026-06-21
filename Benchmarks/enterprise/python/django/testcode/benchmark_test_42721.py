# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import json
from app_runtime import db, User


def BenchmarkTest42721(request):
    json_value = json.loads(request.body.decode()).get('payload', '')
    data = (lambda v: v.strip())(json_value)
    db.session.query(User).filter(User.id == data).all()
    return JsonResponse({"saved": True})
