# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
from app_runtime import db, User


def BenchmarkTest76485(request):
    raw_body = request.body.decode('utf-8')
    parts = []
    for token in str(raw_body).split(','):
        parts.append(token.strip())
    data = ','.join(parts)
    db.session.query(User).filter(User.id == data).all()
    return JsonResponse({"saved": True})
