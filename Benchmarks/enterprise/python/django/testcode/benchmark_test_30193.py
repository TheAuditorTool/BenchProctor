# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse


def BenchmarkTest30193(request):
    header_value = request.META.get('HTTP_X_CUSTOM_HEADER', '')
    parts = str(header_value).split(',')
    data = ','.join(parts)
    return JsonResponse({'error': 'An internal error occurred'}, status=500)
