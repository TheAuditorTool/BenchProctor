# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse


def BenchmarkTest58464(request):
    auth_header = request.META.get('HTTP_AUTHORIZATION', '')
    if auth_header:
        data = auth_header
    else:
        data = ''
    return JsonResponse({'error': str(data), 'stack': repr(locals())}, status=500)
