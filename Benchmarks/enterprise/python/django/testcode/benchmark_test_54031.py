# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse


def BenchmarkTest54031(request):
    host_value = request.META.get('HTTP_HOST', '')
    data = f'{host_value}'
    return JsonResponse({'error': 'An internal error occurred'}, status=500)
