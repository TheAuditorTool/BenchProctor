# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse


def BenchmarkTest11016(request):
    ua_value = request.META.get('HTTP_USER_AGENT', '')
    data = '{}'.format(ua_value)
    return JsonResponse({'error': str(data), 'stack': repr(locals())}, status=500)
