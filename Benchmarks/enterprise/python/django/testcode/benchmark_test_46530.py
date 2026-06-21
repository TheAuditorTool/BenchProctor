# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import os


def BenchmarkTest46530(request):
    header_value = request.META.get('HTTP_X_CUSTOM_HEADER', '')
    os.environ['APP_USER_PREFERENCE'] = str(header_value)
    return JsonResponse({'config_set': 'APP_USER_PREFERENCE'}, status=200)
