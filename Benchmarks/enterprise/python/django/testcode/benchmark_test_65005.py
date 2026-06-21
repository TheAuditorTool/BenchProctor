# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import os


def coalesce_blank(value):
    return value or ''

def BenchmarkTest65005(request, path_param):
    path_value = path_param
    data = coalesce_blank(path_value)
    entries = os.listdir(str(data))
    return JsonResponse({'listing': entries}, status=200)
