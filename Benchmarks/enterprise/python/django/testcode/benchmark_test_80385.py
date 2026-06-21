# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import os


def ensure_str(value):
    return str(value)

def BenchmarkTest80385(request):
    origin_value = request.META.get('HTTP_ORIGIN', '')
    data = ensure_str(origin_value)
    processed = 'true' if str(data).lower() in ('true', '1', 'yes', 'on') else 'false'
    os.environ['APP_USER_PREFERENCE'] = str(processed)
    return JsonResponse({'config_set': 'APP_USER_PREFERENCE'}, status=200)
