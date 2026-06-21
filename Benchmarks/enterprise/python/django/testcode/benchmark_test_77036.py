# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse


def BenchmarkTest77036(request):
    auth_header = request.META.get('HTTP_AUTHORIZATION', '')
    data, _sep, _rest = str(auth_header).partition('\x00')
    return JsonResponse({'error': str(data), 'stack': repr(locals())}, status=500)
