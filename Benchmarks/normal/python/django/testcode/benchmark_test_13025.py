# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse


def BenchmarkTest13025(request):
    host_value = request.META.get('HTTP_HOST', '')
    if host_value:
        data = host_value
    else:
        data = ''
    return JsonResponse({'error': 'An internal error occurred'}, status=500)
