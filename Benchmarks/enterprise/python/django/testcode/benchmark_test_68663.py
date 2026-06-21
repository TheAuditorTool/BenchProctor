# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse


def BenchmarkTest68663(request):
    ua_value = request.META.get('HTTP_USER_AGENT', '')
    data = '%s' % (ua_value,)
    return JsonResponse({'error': 'An internal error occurred'}, status=500)
