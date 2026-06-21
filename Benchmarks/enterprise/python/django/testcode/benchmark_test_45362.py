# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse


def BenchmarkTest45362(request):
    host_value = request.META.get('HTTP_HOST', '')
    data = '%s' % str(host_value)
    return JsonResponse({'error': str(data), 'stack': repr(locals())}, status=500)
