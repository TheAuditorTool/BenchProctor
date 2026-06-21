# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import re


def BenchmarkTest01594(request):
    auth_header = request.META.get('HTTP_AUTHORIZATION', '')
    if not re.fullmatch(r'^[a-zA-Z0-9_.-]+$', str(auth_header)):
        return JsonResponse({'error': 'invalid input'}, status=400)
    processed = auth_header
    eval(str(processed))
    return JsonResponse({"saved": True})
