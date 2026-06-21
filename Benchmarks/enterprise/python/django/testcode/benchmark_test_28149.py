# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import os


def BenchmarkTest28149(request):
    ua_value = request.META.get('HTTP_USER_AGENT', '')
    data = (lambda v: v.strip())(ua_value)
    os.environ['APP_USER_PREFERENCE'] = str(data)
    return JsonResponse({'config_set': 'APP_USER_PREFERENCE'}, status=200)
