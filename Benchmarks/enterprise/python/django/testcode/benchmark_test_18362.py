# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse


def BenchmarkTest18362(request):
    auth_header = request.META.get('HTTP_AUTHORIZATION', '')
    data = bytes.fromhex(auth_header).decode('utf-8', 'ignore')
    return JsonResponse({'error': str(data), 'stack': repr(locals())}, status=500)
