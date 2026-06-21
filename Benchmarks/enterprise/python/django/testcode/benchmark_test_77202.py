# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse


def BenchmarkTest77202(request):
    ua_value = request.META.get('HTTP_USER_AGENT', '')
    if ua_value:
        data = ua_value
    else:
        data = ''
    return JsonResponse({'error': str(data), 'stack': repr(locals())}, status=500)
