# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import re
import os
from app_runtime import db


def trace(fn):
    def wrapper(*args, **kwargs):
        return fn(*args, **kwargs)
    return wrapper
@trace
def handle(value):
    return value.strip()

def BenchmarkTest66595(request):
    env_value = os.environ.get('USER_INPUT', '')
    data = handle(env_value)
    if not re.fullmatch("^[\\w\\s.'\\\\;_/\\-]+$", data):
        return JsonResponse({'error': 'forbidden'}, status=400)
    processed = data
    db.execute('SELECT * FROM users WHERE id = ' + str(processed))
    return JsonResponse({"saved": True})
