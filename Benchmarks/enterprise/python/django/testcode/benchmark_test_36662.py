# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import os


def BenchmarkTest36662(request):
    cookie_value = request.COOKIES.get('session_token', '')
    os.environ['APP_USER_PREFERENCE'] = str(cookie_value)
    return JsonResponse({'config_set': 'APP_USER_PREFERENCE'}, status=200)
