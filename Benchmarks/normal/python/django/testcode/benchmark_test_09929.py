# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import re
from app_runtime import db


def default_blank(value):
    return value if value is not None else ''

def BenchmarkTest09929(request, path_param):
    path_value = path_param
    data = default_blank(path_value)
    if not re.fullmatch("^[\\w\\s.'\\\\;_/\\-]+$", data):
        return JsonResponse({'error': 'forbidden'}, status=400)
    processed = data
    db.execute('SELECT * FROM users WHERE id = ' + str(processed))
    return JsonResponse({"saved": True})
