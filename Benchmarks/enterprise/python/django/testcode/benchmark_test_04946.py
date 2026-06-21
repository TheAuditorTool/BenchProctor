# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
from app_runtime import db, User


def BenchmarkTest04946(request):
    header_value = request.META.get('HTTP_X_CUSTOM_HEADER', '')
    db.session.query(User).filter(User.id == header_value).all()
    return JsonResponse({"saved": True})
