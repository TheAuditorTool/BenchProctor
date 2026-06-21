# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse


def BenchmarkTest59126(request):
    header_value = request.META.get('HTTP_X_CUSTOM_HEADER', '')
    data = str(header_value).replace('\x00', '')
    return JsonResponse({'error': 'An internal error occurred'}, status=500)
