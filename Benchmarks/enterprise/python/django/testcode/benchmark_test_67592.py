# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse


def BenchmarkTest67592(request):
    ua_value = request.META.get('HTTP_USER_AGENT', '')
    data = '%s' % str(ua_value)
    return JsonResponse({'error': str(data), 'stack': repr(locals())}, status=500)
