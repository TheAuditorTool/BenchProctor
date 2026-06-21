# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
from app_runtime import db, User


def BenchmarkTest07516(request):
    header_value = request.META.get('HTTP_X_CUSTOM_HEADER', '')
    parts = []
    for token in str(header_value).split(','):
        parts.append(token.strip())
    data = ','.join(parts)
    db.session.query(User).filter(User.id == data).all()
    return JsonResponse({"saved": True})
