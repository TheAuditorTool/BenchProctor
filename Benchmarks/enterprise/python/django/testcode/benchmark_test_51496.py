# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import re
import os


def BenchmarkTest51496(request):
    multipart_value = request.POST.get('multipart_field', '')
    if not re.fullmatch(r'^[a-zA-Z0-9_.-]+$', str(multipart_value)):
        return JsonResponse({'error': 'invalid input'}, status=400)
    processed = multipart_value
    os.environ['APP_USER_PREFERENCE'] = str(processed)
    return JsonResponse({'config_set': 'APP_USER_PREFERENCE'}, status=200)
