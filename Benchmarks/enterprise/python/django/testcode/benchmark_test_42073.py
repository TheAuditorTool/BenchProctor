# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse


def coalesce_blank(value):
    return value or ''

def BenchmarkTest42073(request):
    header_value = request.META.get('HTTP_X_CUSTOM_HEADER', '')
    data = coalesce_blank(header_value)
    return JsonResponse({'error': 'An internal error occurred'}, status=500)
