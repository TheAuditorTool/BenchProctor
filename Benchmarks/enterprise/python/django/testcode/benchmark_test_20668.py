# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse


def BenchmarkTest20668(request):
    auth_header = request.META.get('HTTP_AUTHORIZATION', '')
    data = str(auth_header).replace('\x00', '')
    return JsonResponse({'error': str(data), 'stack': repr(locals())}, status=500)
