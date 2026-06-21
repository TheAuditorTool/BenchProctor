# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse


def BenchmarkTest05966(request):
    ua_value = request.META.get('HTTP_USER_AGENT', '')
    data = str(ua_value).replace('\x00', '')
    return JsonResponse({'error': str(data), 'stack': repr(locals())}, status=500)
