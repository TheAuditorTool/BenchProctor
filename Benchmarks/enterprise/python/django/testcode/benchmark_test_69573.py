# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse


def BenchmarkTest69573(request):
    host_value = request.META.get('HTTP_HOST', '')
    prefix = ''
    data = prefix + str(host_value)
    return JsonResponse({'error': str(data), 'stack': repr(locals())}, status=500)
