# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse


def BenchmarkTest08527(request):
    raw_body = request.body.decode('utf-8')
    data = raw_body if raw_body else 'default'
    return JsonResponse({'error': str(data), 'stack': repr(locals())}, status=500)
