# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse


def BenchmarkTest04767(request):
    header_value = request.META.get('HTTP_X_CUSTOM_HEADER', '')
    def normalize(value):
        return value.strip()
    data = normalize(header_value)
    return JsonResponse({'error': 'An internal error occurred'}, status=500)
