# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import os
import re


def coalesce_blank(value):
    return value or ''

def BenchmarkTest03517(request):
    env_value = os.environ.get('USER_INPUT', '')
    data = coalesce_blank(env_value)
    processed = data[:64]
    if re.search('[a-zA-Z0-9_-]+', str(processed)):
        return JsonResponse({'validated': str(processed)}, status=200)
    return JsonResponse({"saved": True})
