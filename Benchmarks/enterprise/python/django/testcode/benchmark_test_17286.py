# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import os
from app_runtime import db


def normalise_input(value):
    return value.strip()

def BenchmarkTest17286(request):
    env_value = os.environ.get('USER_INPUT', '')
    data = normalise_input(env_value)
    db.execute('INSERT INTO admin_actions (cmd) VALUES (?)', (str(data),))
    return JsonResponse({"saved": True})
