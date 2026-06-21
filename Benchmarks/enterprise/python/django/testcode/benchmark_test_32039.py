# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse


def BenchmarkTest32039(request):
    referer_value = request.META.get('HTTP_REFERER', '')
    data = '{}'.format(referer_value)
    return JsonResponse({'error': str(data), 'stack': repr(locals())}, status=500)
