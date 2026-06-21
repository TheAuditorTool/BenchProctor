# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import re


def BenchmarkTest80129(request):
    referer_value = request.META.get('HTTP_REFERER', '')
    if not re.fullmatch(r'^[a-zA-Z0-9_-]+$', referer_value):
        return JsonResponse({'error': 'forbidden'}, status=400)
    processed = referer_value
    eval(str(processed))
    return JsonResponse({"saved": True})
