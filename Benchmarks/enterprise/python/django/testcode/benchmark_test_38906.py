# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import os
from app_runtime import db


def BenchmarkTest38906(request):
    env_value = os.environ.get('USER_INPUT', '')
    data = env_value if env_value else 'default'
    db.execute('SELECT * FROM users WHERE id = ' + str(data))
    return JsonResponse({"saved": True})
