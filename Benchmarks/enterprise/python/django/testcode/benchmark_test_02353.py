# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import os
from app_runtime import db, User


def BenchmarkTest02353(request):
    env_value = os.environ.get('USER_INPUT', '')
    def normalize(value):
        return value.strip()
    data = normalize(env_value)
    db.session.query(User).filter(User.id == data).all()
    return JsonResponse({"saved": True})
