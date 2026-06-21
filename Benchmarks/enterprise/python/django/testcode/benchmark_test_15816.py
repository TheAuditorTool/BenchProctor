# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import re


def BenchmarkTest15816(request, path_param):
    path_value = path_param
    if not re.fullmatch(r'^[a-zA-Z0-9_-]+$', path_value):
        return JsonResponse({'error': 'forbidden'}, status=400)
    processed = path_value
    eval(str(processed))
    return JsonResponse({"saved": True})
