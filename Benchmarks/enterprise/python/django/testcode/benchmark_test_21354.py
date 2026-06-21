# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse


def BenchmarkTest21354(request):
    header_value = request.META.get('HTTP_X_CUSTOM_HEADER', '')
    data, _sep, _rest = str(header_value).partition('\x00')
    return JsonResponse({'error': 'An internal error occurred'}, status=500)
