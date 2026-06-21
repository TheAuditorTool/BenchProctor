# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse


def BenchmarkTest27129(request):
    header_value = request.META.get('HTTP_X_CUSTOM_HEADER', '')
    prefix = ''
    data = prefix + str(header_value)
    return JsonResponse({'error': 'An internal error occurred'}, status=500)
