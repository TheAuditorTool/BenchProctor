# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse


def BenchmarkTest03301(request):
    host_value = request.META.get('HTTP_HOST', '')
    data = host_value if host_value else 'default'
    return JsonResponse({'error': str(data), 'stack': repr(locals())}, status=500)
