# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import os


def BenchmarkTest00017(request, path_param):
    path_value = path_param
    data = f'{path_value}'
    entries = os.listdir(str(data))
    return JsonResponse({'listing': entries}, status=200)
