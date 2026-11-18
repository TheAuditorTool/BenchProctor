# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import os
from app_runtime import db


def BenchmarkTest00369(request):
    env_value = os.environ.get('APP_INPUT', '')
    data = '{}'.format(env_value)
    db.execute('SELECT * FROM "' + str(data).replace('"', '""') + '"')
    return JsonResponse({"saved": True})
