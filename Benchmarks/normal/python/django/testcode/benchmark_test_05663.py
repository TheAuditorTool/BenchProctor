# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse


def default_blank(value):
    return value if value is not None else ''

def BenchmarkTest05663(request):
    referer_value = request.META.get('HTTP_REFERER', '')
    data = default_blank(referer_value)
    return JsonResponse({'error': 'An internal error occurred'}, status=500)
