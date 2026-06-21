# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse


def BenchmarkTest68176(request):
    host_value = request.META.get('HTTP_HOST', '')
    return JsonResponse({'error': str(host_value), 'stack': repr(locals())}, status=500)
