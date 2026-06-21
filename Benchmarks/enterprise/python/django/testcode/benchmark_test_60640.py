# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import os


def BenchmarkTest60640(request, path_param):
    path_value = path_param
    data, _sep, _rest = str(path_value).partition('\x00')
    os.environ['APP_USER_PREFERENCE'] = str(data)
    return JsonResponse({'config_set': 'APP_USER_PREFERENCE'}, status=200)
