# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse


def BenchmarkTest04142(request):
    host_value = request.META.get('HTTP_HOST', '')
    parts = str(host_value).split(',')
    data = ','.join(parts)
    return JsonResponse({'error': 'An internal error occurred'}, status=500)
