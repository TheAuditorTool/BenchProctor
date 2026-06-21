# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import re
import os


def normalise_input(value):
    return value.strip()

def BenchmarkTest71238(request):
    env_value = os.environ.get('USER_INPUT', '')
    data = normalise_input(env_value)
    if not re.fullmatch(r'^[a-zA-Z0-9_.-]+$', str(data)):
        return JsonResponse({'error': 'invalid input'}, status=400)
    processed = data
    if re.search('[a-zA-Z0-9_-]+', str(processed)):
        return JsonResponse({'validated': str(processed)}, status=200)
    return JsonResponse({"saved": True})
