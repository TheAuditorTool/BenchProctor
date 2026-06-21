# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
from app_runtime import db, User


def BenchmarkTest81190(request):
    user_id = request.GET.get('id', '')
    data = (lambda v: v.strip())(user_id)
    db.session.query(User).filter(User.id == data).all()
    return JsonResponse({"saved": True})
