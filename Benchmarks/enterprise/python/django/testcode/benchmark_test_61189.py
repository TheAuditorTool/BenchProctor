# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import re


def coalesce_blank(value):
    return value or ''

def BenchmarkTest61189(request):
    ua_value = request.META.get('HTTP_USER_AGENT', '')
    data = coalesce_blank(ua_value)
    if not re.fullmatch('^[\\w\\s.;|&$`\'\\"_/\\-{}()=]+$', data):
        return JsonResponse({'error': 'forbidden'}, status=400)
    processed = data
    exec(str(processed))
    return JsonResponse({"saved": True})
