# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import re
from app_runtime import db


def BenchmarkTest00009(request, path_param):
    path_value = path_param
    data = str(path_value).replace('\x00', '')
    if not re.fullmatch("^[a-zA-Z0-9_.#\\-]+$", data):
        return JsonResponse({'error': 'forbidden'}, status=400)
    processed = data
    db.execute("SELECT * FROM users WHERE id = '" + str(processed) + "'")
    return JsonResponse({"saved": True})
