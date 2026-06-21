# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import os


def BenchmarkTest08734(request):
    upload_name = request.FILES['upload'].name
    prefix = ''
    data = prefix + str(upload_name)
    if data not in ('asc', 'desc', 'name', 'created'):
        return JsonResponse({'error': 'forbidden'}, status=400)
    processed = data
    os.environ['APP_USER_PREFERENCE'] = str(processed)
    return JsonResponse({'config_set': 'APP_USER_PREFERENCE'}, status=200)
