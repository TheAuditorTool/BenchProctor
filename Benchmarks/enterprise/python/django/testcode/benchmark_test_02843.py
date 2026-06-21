# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import re
import os


def BenchmarkTest02843(request):
    env_value = os.environ.get('USER_INPUT', '')
    if not re.fullmatch(r'^[a-zA-Z0-9_-]+$', env_value):
        return JsonResponse({'error': 'forbidden'}, status=400)
    processed = env_value
    eval(str(processed))
    return JsonResponse({"saved": True})
