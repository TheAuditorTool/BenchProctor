# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse


def BenchmarkTest70675(request):
    host_value = request.META.get('HTTP_HOST', '')
    data = f'{host_value}'
    return JsonResponse({'error': str(data), 'stack': repr(locals())}, status=500)
