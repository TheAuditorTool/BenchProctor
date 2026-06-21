# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import os
from app_runtime import db


def BenchmarkTest12980(request):
    env_value = os.environ.get('USER_INPUT', '')
    db.execute('SELECT * FROM "' + str(env_value).replace('"', '""') + '"')
    return JsonResponse({"saved": True})
