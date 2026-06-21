# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse


def BenchmarkTest23480(request):
    host_value = request.META.get('HTTP_HOST', '')
    data = (lambda v: v.strip())(host_value)
    return JsonResponse({'error': str(data), 'stack': repr(locals())}, status=500)
