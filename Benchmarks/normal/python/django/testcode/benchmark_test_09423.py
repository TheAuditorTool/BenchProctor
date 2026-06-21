# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import base64
from app_runtime import db, User


def BenchmarkTest09423(request):
    auth_header = request.META.get('HTTP_AUTHORIZATION', '')
    data = base64.b64decode(auth_header).decode('utf-8', 'ignore')
    db.session.query(User).filter(User.id == data).all()
    return JsonResponse({"saved": True})
