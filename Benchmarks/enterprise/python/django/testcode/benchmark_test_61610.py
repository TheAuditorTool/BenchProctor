# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import re


def to_text(value):
    return str(value).strip()

def BenchmarkTest61610(request):
    host_value = request.META.get('HTTP_HOST', '')
    data = to_text(host_value)
    if not re.fullmatch('^[\\w\\s.,;:_/\\-=]+$', data):
        return JsonResponse({'error': 'forbidden'}, status=400)
    processed = data
    return JsonResponse({'error': str(processed), 'stack': repr(locals())}, status=500)
