# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse


def BenchmarkTest71312(request):
    ua_value = request.META.get('HTTP_USER_AGENT', '')
    parts = str(ua_value).split(',')
    data = ','.join(parts)
    return JsonResponse({'error': str(data), 'stack': repr(locals())}, status=500)
