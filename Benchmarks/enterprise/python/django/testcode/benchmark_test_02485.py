# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import os


def BenchmarkTest02485(request):
    xml_value = request.body.decode('utf-8')
    data = ' '.join(str(xml_value).split())
    if data not in ('asc', 'desc', 'name', 'created'):
        return JsonResponse({'error': 'forbidden'}, status=400)
    processed = data
    os.environ['APP_USER_PREFERENCE'] = str(processed)
    return JsonResponse({'config_set': 'APP_USER_PREFERENCE'}, status=200)
