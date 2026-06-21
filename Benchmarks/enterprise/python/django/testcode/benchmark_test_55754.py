# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse


def BenchmarkTest55754(request):
    ua_value = request.META.get('HTTP_USER_AGENT', '')
    prefix = ''
    data = prefix + str(ua_value)
    return JsonResponse({'error': str(data), 'stack': repr(locals())}, status=500)
