# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import os


def normalise_input(value):
    return value.strip()

def BenchmarkTest44880(request, path_param):
    path_value = path_param
    data = normalise_input(path_value)
    os.remove(str(data))
    return JsonResponse({"saved": True})
