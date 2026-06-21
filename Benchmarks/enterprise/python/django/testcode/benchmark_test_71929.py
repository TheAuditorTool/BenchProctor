# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse


def BenchmarkTest71929(request):
    auth_header = request.META.get('HTTP_AUTHORIZATION', '')
    parts = str(auth_header).split(',')
    data = ','.join(parts)
    return JsonResponse({'error': str(data), 'stack': repr(locals())}, status=500)
