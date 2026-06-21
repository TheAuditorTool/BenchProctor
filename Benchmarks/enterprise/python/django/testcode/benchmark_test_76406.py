# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import os


def BenchmarkTest76406(request, path_param):
    path_value = path_param
    data = str(path_value).replace('\x00', '')
    entries = os.listdir(str(data))
    return JsonResponse({'listing': entries}, status=200)
