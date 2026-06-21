# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import os


def BenchmarkTest08597(request, path_param):
    path_value = path_param
    if path_value:
        data = path_value
    else:
        data = ''
    entries = os.listdir(str(data))
    return JsonResponse({'listing': entries}, status=200)
