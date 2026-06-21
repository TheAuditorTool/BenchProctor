# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import os
from app_runtime import db


def BenchmarkTest36157(request):
    env_value = os.environ.get('USER_INPUT', '')
    parts = []
    for token in str(env_value).split(','):
        parts.append(token.strip())
    data = ','.join(parts)
    db.execute('UPDATE users SET password = ? WHERE id = 1', (str(data),))
    return JsonResponse({"saved": True})
