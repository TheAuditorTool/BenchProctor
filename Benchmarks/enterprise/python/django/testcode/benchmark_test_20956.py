# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse


def BenchmarkTest20956(request):
    referer_value = request.META.get('HTTP_REFERER', '')
    data = '%s' % str(referer_value)
    return JsonResponse({'error': str(data), 'stack': repr(locals())}, status=500)
