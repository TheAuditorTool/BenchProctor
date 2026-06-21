# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse


def BenchmarkTest03404(request):
    origin_value = request.META.get('HTTP_ORIGIN', '')
    data = '%s' % (origin_value,)
    return JsonResponse({'error': str(data), 'stack': repr(locals())}, status=500)
