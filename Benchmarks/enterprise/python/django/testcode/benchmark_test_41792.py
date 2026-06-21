# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import os
from app_runtime import db


def BenchmarkTest41792(request):
    env_value = os.environ.get('USER_INPUT', '')
    db.execute('UPDATE users SET password = ? WHERE id = 1', (str(env_value),))
    return JsonResponse({"saved": True})
