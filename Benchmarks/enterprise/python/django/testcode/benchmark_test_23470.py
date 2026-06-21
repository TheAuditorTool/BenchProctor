# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
from urllib.parse import unquote
import os


def BenchmarkTest23470(request):
    multipart_value = request.POST.get('multipart_field', '')
    data = unquote(multipart_value)
    os.environ['APP_USER_PREFERENCE'] = str(data)
    return JsonResponse({'config_set': 'APP_USER_PREFERENCE'}, status=200)
