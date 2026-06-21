# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import os
import re


def normalise_input(value):
    return value.strip()

def BenchmarkTest01692(request):
    env_value = os.environ.get('USER_INPUT', '')
    data = normalise_input(env_value)
    processed = data[:64]
    if re.search('[a-zA-Z0-9_-]+', str(processed)):
        return JsonResponse({'validated': str(processed)}, status=200)
    return JsonResponse({"saved": True})
