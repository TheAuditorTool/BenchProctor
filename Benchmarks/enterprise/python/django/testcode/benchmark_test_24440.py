# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import os


def to_text(value):
    return str(value).strip()

def BenchmarkTest24440(request):
    auth_header = request.META.get('HTTP_AUTHORIZATION', '')
    data = to_text(auth_header)
    processed = data[:64]
    os.environ['APP_USER_PREFERENCE'] = str(processed)
    return JsonResponse({'config_set': 'APP_USER_PREFERENCE'}, status=200)
