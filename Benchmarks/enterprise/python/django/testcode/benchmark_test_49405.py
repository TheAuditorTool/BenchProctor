# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import re


def coalesce_blank(value):
    return value or ''

def BenchmarkTest49405(request):
    referer_value = request.META.get('HTTP_REFERER', '')
    data = coalesce_blank(referer_value)
    if not re.fullmatch('^[\\w\\s.,;:_/\\-=]+$', data):
        return JsonResponse({'error': 'forbidden'}, status=400)
    processed = data
    return JsonResponse({'error': str(processed), 'stack': repr(locals())}, status=500)
