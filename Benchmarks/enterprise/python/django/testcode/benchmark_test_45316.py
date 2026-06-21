# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse


def BenchmarkTest45316(request):
    auth_header = request.META.get('HTTP_AUTHORIZATION', '')
    data, _sep, _rest = str(auth_header).partition('\x00')
    return JsonResponse({'error': 'An internal error occurred'}, status=500)
