# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
from app_runtime import db, User


def BenchmarkTest51227(request):
    upload_name = request.FILES['upload'].name
    data = str(upload_name).replace('\x00', '')
    db.session.query(User).filter(User.id == data).all()
    return JsonResponse({"saved": True})
