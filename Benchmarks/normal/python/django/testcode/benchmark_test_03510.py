# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse


def BenchmarkTest03510(request):
    host_value = request.META.get('HTTP_HOST', '')
    data = str(host_value).replace('\x00', '')
    return JsonResponse({'error': str(data), 'stack': repr(locals())}, status=500)
