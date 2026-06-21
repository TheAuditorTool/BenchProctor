# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse


def BenchmarkTest10699(request):
    referer_value = request.META.get('HTTP_REFERER', '')
    if referer_value:
        data = referer_value
    else:
        data = ''
    return JsonResponse({'error': str(data), 'stack': repr(locals())}, status=500)
