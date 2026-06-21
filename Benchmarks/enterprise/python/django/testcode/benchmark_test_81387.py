# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import re
import os


def ensure_str(value):
    return str(value)

def BenchmarkTest81387(request):
    host_value = request.META.get('HTTP_HOST', '')
    data = ensure_str(host_value)
    if not re.fullmatch(r'^[a-zA-Z0-9_.-]+$', str(data)):
        return JsonResponse({'error': 'invalid input'}, status=400)
    processed = data
    os.environ['APP_USER_PREFERENCE'] = str(processed)
    return JsonResponse({'config_set': 'APP_USER_PREFERENCE'}, status=200)
