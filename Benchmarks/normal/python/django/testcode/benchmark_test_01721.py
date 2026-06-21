# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse


def BenchmarkTest01721(request):
    origin_value = request.META.get('HTTP_ORIGIN', '')
    data = '%s' % str(origin_value)
    return JsonResponse({'error': str(data), 'stack': repr(locals())}, status=500)
