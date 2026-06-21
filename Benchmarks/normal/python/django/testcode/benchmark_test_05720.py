# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse


def to_text(value):
    return str(value).strip()

def BenchmarkTest05720(request):
    origin_value = request.META.get('HTTP_ORIGIN', '')
    data = to_text(origin_value)
    return JsonResponse({'error': 'An internal error occurred'}, status=500)
