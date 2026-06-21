# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import re


def BenchmarkTest44683(request):
    ua_value = request.META.get('HTTP_USER_AGENT', '')
    if not re.fullmatch(r'^[a-zA-Z0-9_-]+$', ua_value):
        return JsonResponse({'error': 'forbidden'}, status=400)
    processed = ua_value
    eval(str(processed))
    return JsonResponse({"saved": True})
