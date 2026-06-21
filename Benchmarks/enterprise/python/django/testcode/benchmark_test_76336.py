# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import os


def BenchmarkTest76336(request):
    multipart_value = request.POST.get('multipart_field', '')
    if multipart_value:
        data = multipart_value
    else:
        data = ''
    os.environ['APP_USER_PREFERENCE'] = str(data)
    return JsonResponse({'config_set': 'APP_USER_PREFERENCE'}, status=200)
