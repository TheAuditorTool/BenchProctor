# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import re


def default_blank(value):
    return value if value is not None else ''

def BenchmarkTest51497(request):
    forwarded_ip = request.META.get('HTTP_X_FORWARDED_FOR', '')
    data = default_blank(forwarded_ip)
    if not re.fullmatch(r'^[a-zA-Z0-9_-]+$', data):
        return JsonResponse({'error': 'forbidden'}, status=400)
    processed = data
    exec(str(processed))
    return JsonResponse({"saved": True})
