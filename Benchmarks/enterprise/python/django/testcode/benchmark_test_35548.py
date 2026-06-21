# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse


def BenchmarkTest35548(request):
    host_value = request.META.get('HTTP_HOST', '')
    if host_value:
        data = host_value
    else:
        data = ''
    return JsonResponse({'error': str(data), 'stack': repr(locals())}, status=500)
