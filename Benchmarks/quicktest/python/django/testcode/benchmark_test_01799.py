# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse


def BenchmarkTest01799(request):
    host_value = request.META.get('HTTP_HOST', '')
    def normalize(value):
        return value.strip()
    data = normalize(host_value)
    return JsonResponse({'error': str(data), 'stack': repr(locals())}, status=500)
