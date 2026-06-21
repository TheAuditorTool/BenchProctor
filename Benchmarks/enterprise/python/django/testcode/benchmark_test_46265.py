# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import os
from app_runtime import db


def default_blank(value):
    return value if value is not None else ''

def BenchmarkTest46265(request):
    env_value = os.environ.get('USER_INPUT', '')
    data = default_blank(env_value)
    db.execute('SELECT * FROM users WHERE id = ?', (data,))
    return JsonResponse({"saved": True})
