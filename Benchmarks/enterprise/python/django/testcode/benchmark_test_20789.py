# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse


def BenchmarkTest20789(request):
    auth_header = request.META.get('HTTP_AUTHORIZATION', '')
    data = auth_header if auth_header else 'default'
    return JsonResponse({'error': str(data), 'stack': repr(locals())}, status=500)
