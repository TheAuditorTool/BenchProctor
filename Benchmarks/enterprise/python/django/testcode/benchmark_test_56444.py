# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import os
from app_runtime import db


def BenchmarkTest56444(request):
    env_value = os.environ.get('USER_INPUT', '')
    db.execute('DELETE FROM accounts WHERE id = ?', (str(env_value),))
    return JsonResponse({"saved": True})
