# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import os


def BenchmarkTest78420(request):
    xml_value = request.body.decode('utf-8')
    os.environ['APP_USER_PREFERENCE'] = str(xml_value)
    return JsonResponse({'config_set': 'APP_USER_PREFERENCE'}, status=200)
