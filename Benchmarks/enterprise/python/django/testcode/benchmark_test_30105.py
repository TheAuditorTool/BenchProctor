# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import os
from app_runtime import db, User


def BenchmarkTest30105(request):
    env_value = os.environ.get('USER_INPUT', '')
    data, _sep, _rest = str(env_value).partition('\x00')
    db.session.query(User).filter(User.id == data).all()
    return JsonResponse({"saved": True})
