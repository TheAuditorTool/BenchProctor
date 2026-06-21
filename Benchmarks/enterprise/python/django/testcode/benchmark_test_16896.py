# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse


def BenchmarkTest16896(request):
    ua_value = request.META.get('HTTP_USER_AGENT', '')
    return JsonResponse({'error': str(ua_value), 'stack': repr(locals())}, status=500)
