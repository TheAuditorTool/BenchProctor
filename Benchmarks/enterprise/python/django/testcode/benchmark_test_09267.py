# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import re
import os


def ensure_str(value):
    return str(value)

def BenchmarkTest09267(request):
    user_id = request.GET.get('id', '')
    data = ensure_str(user_id)
    if not re.fullmatch(r'^[a-zA-Z0-9_-]+$', data):
        return JsonResponse({'error': 'forbidden'}, status=400)
    processed = data
    os.environ['APP_USER_PREFERENCE'] = str(processed)
    return JsonResponse({'config_set': 'APP_USER_PREFERENCE'}, status=200)
