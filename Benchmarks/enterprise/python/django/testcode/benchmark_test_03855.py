# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse


def ensure_str(value):
    return str(value)

def BenchmarkTest03855(request):
    host_value = request.META.get('HTTP_HOST', '')
    data = ensure_str(host_value)
    return JsonResponse({'error': str(data), 'stack': repr(locals())}, status=500)
