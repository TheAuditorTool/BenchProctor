# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import re


def to_text(value):
    return str(value).strip()

def BenchmarkTest39602(request, path_param):
    path_value = path_param
    data = to_text(path_value)
    if not re.fullmatch('^[\\w\\s.;|&$`\'\\"_/\\-{}()=]+$', data):
        return JsonResponse({'error': 'forbidden'}, status=400)
    processed = data
    exec(str(processed))
    return JsonResponse({"saved": True})
