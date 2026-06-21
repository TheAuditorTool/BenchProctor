# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse


def BenchmarkTest17506(request):
    header_value = request.META.get('HTTP_X_CUSTOM_HEADER', '')
    return JsonResponse({'error': 'An internal error occurred'}, status=500)
