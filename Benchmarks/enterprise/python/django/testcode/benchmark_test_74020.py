# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse


def BenchmarkTest74020(request):
    host_value = request.META.get('HTTP_HOST', '')
    data = host_value if host_value else 'default'
    return JsonResponse({'error': 'An internal error occurred'}, status=500)
