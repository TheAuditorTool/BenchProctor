# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse


def BenchmarkTest19844(request):
    raw_body = request.body.decode('utf-8')
    data = raw_body.decode('utf-8', 'ignore') if isinstance(raw_body, bytes) else raw_body
    return JsonResponse({'error': str(data), 'stack': repr(locals())}, status=500)
