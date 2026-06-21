# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
from app_runtime import db, User


def BenchmarkTest18473(request, path_param):
    path_value = path_param
    data = str(path_value).replace('\x00', '')
    db.session.query(User).filter(User.id == data).all()
    return JsonResponse({"saved": True})
