# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import re


def default_blank(value):
    return value if value is not None else ''

def BenchmarkTest27887(request):
    ua_value = request.META.get('HTTP_USER_AGENT', '')
    data = default_blank(ua_value)
    if not re.fullmatch(r'^[a-zA-Z0-9_.-]+$', str(data)):
        return JsonResponse({'error': 'invalid input'}, status=400)
    processed = data
    exec(str(processed))
    return JsonResponse({"saved": True})
