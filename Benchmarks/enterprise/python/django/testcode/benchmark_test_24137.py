# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import os
from app_runtime import db, User


def BenchmarkTest24137(request):
    env_value = os.environ.get('USER_INPUT', '')
    data = env_value if env_value else 'default'
    db.session.query(User).filter(User.id == data).all()
    return JsonResponse({"saved": True})
