# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import os
from app_runtime import db


def BenchmarkTest19312(request):
    env_value = os.environ.get('USER_INPUT', '')
    collected = None
    def on_input(value):
        nonlocal collected
        collected = value
    on_input(env_value)
    data = collected
    db.execute('UPDATE users SET role = ? WHERE name = ?', ('admin', str(data)))
    return JsonResponse({"saved": True})
