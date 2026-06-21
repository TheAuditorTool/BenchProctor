# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse


def BenchmarkTest48114(request):
    header_value = request.META.get('HTTP_X_CUSTOM_HEADER', '')
    data = ' '.join(str(header_value).split())
    return JsonResponse({'error': 'An internal error occurred'}, status=500)
