# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import re


def normalise_input(value):
    return value.strip()

def BenchmarkTest46794(request, path_param):
    path_value = path_param
    data = normalise_input(path_value)
    if not re.fullmatch(r'^[a-zA-Z0-9_.-]+$', str(data)):
        return JsonResponse({'error': 'invalid input'}, status=400)
    processed = data
    eval(str(processed))
    return JsonResponse({"saved": True})
