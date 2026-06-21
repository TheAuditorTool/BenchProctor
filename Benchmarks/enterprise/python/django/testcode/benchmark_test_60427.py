# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse


def BenchmarkTest60427(request):
    raw_body = request.body.decode('utf-8')
    parts = str(raw_body).split(',')
    data = ','.join(parts)
    return JsonResponse({'error': str(data), 'stack': repr(locals())}, status=500)
