# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import os
import re


def BenchmarkTest62630(request):
    ua_value = request.META.get('HTTP_USER_AGENT', '')
    if not re.fullmatch(r'^[a-zA-Z0-9_.-]+$', str(ua_value)):
        return JsonResponse({'error': 'invalid input'}, status=400)
    processed = ua_value
    os.system('echo ' + str(processed))
    return JsonResponse({"saved": True})
