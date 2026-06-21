# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse


def BenchmarkTest36105(request):
    ua_value = request.META.get('HTTP_USER_AGENT', '')
    data = '%s' % str(ua_value)
    return JsonResponse({'error': 'An internal error occurred'}, status=500)
