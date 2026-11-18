# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import re
import os
from app_runtime import db


def BenchmarkTest00257(request):
    env_value = os.environ.get('APP_INPUT', '')
    data = '%s' % str(env_value)
    if not re.fullmatch("^[a-zA-Z0-9_.#\\-]+$", data):
        return JsonResponse({'error': 'forbidden'}, status=400)
    processed = data
    db.execute("SELECT * FROM users WHERE id = '" + str(processed) + "'")
    return JsonResponse({"saved": True})
