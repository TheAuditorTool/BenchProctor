# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import re
import os


def coalesce_blank(value):
    return value or ''

def BenchmarkTest66991(request):
    env_value = os.environ.get('USER_INPUT', '')
    data = coalesce_blank(env_value)
    if not re.fullmatch(r'^[a-zA-Z0-9_-]+$', data):
        return JsonResponse({'error': 'forbidden'}, status=400)
    processed = data
    eval(str(processed))
    return JsonResponse({"saved": True})
