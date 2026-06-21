# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
from app_runtime import db, User


def BenchmarkTest51568(request):
    referer_value = request.META.get('HTTP_REFERER', '')
    data, _sep, _rest = str(referer_value).partition('\x00')
    db.session.query(User).filter(User.id == data).all()
    return JsonResponse({"saved": True})
